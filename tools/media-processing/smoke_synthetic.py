"""Fixed, original synthetic speech only. No input arguments or private data."""
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time
import unicodedata

from transcribe import run, pcm_samples
from batch import process

TEXT = "O computador guarda dados na memória. O teclado permite escrever palavras. A tela mostra uma imagem colorida."
EXPECTED = {"computador", "dados", "memoria", "teclado", "escrever", "palavras", "tela", "imagem", "colorida"}

def tokens(text):
    normalized = unicodedata.normalize("NFKD", text.lower())
    return set(re.findall(r"[a-z]+", "".join(c for c in normalized if not unicodedata.combining(c))))

def main():
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise SystemExit("This smoke test is designed for the isolated CI runner.")
    with tempfile.TemporaryDirectory(prefix="pythoteca-synthetic-") as tmp:
        root = Path(tmp)
        source = root / "synthetic.wav"
        output = root / "synthetic.json"
        subprocess.run(["espeak-ng", "-v", "pt-br", "-s", "145", "-w", str(source), TEXT], check=True)
        print("Synthetic speech generated.", flush=True)
        # Exercise PCM reader independently with a known normalized waveform.
        import wave
        import struct
        import numpy as np
        fixture = root / "pcm-fixture.wav"
        with wave.open(str(fixture), "wb") as wav:
            wav.setparams((1, 2, 16000, 4, "NONE", "not compressed"))
            wav.writeframes(struct.pack("<4h", -32768, 0, 16384, 32767))
        assert np.allclose(pcm_samples(fixture), [-1, 0, .5, 32767/32768])
        print("PCM normalization verified.", flush=True)
        started = time.monotonic()
        # Only the fixed generated file enters the engine. The private CLI remains disabled in CI.
        run(source, output, model="small", model_dir=root / "models")
        elapsed = time.monotonic() - started
        data = json.loads(output.read_text(encoding="utf-8"))
        segments = data["segments"]
        assert data["language"] == "pt" and data["model"] == "small"
        assert segments and all(0 <= s["start"] <= s["end"] for s in segments)
        assert all(isinstance(s["text"], str) for s in segments)
        assert all(a["start"] <= b["start"] for a, b in zip(segments, segments[1:]))
        matched = len(tokens(" ".join(s["text"] for s in segments)) & EXPECTED)
        print(f"Segments: {len(segments)}; keywords: {matched}/{len(EXPECTED)}; engine + download: {elapsed:.1f}s", flush=True)
        if matched < 6:
            raise SystemExit("Synthetic speech recognition below smoke-test threshold.")
        print("Synthetic transcription smoke test passed.")
        inputs = root / "batch-input"
        inputs.mkdir()
        results = root / "batch-results"
        import shutil
        shutil.copyfile(source, inputs / "a.wav")
        shutil.copyfile(source, inputs / "duplicate.wav")
        subprocess.run(["espeak-ng", "-v", "pt-br", "-s", "145", "-w", str(inputs / "b.wav"), "Um programa pode organizar arquivos e pastas."], check=True)
        (inputs / "invalid.wav").write_bytes(b"invalid synthetic audio")
        first = process(inputs, results, model="small", model_dir=root/"models")
        second = process(inputs, results, model="small", model_dir=root/"models")
        assert first == {"processed":2,"skipped":1,"failed":1}, first
        assert second == {"processed":0,"skipped":3,"failed":1}, second
        for folder in results.iterdir():
            assert (folder/"transcript.txt").read_text().strip()
            assert "-->" in (folder/"transcript.srt").read_text()
            assert json.loads((folder/"transcript.json").read_text())["segments"]
        print(f"Batch initial: {first}; resumed: {second}", flush=True)
        print("Synthetic batch smoke test passed.")

if __name__ == "__main__":
    main()
