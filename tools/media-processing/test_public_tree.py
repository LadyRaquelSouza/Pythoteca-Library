import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]/"scripts"))
from validate_public_tree import allowed

class PublicTreeTests(unittest.TestCase):
    def test_allowed(self):
        for path in ["modules/aula109.json", "catalog/index.json", "docs/editorial/intercambio.md", "tools/media-processing/transcribe.py"]:
            self.assertTrue(allowed(path))

    def test_rejected(self):
        for path in ["source.pdf", "private/audio.mp4", "modules/transcript.json", ".env", "credentials.json", "tools/media-processing/transcript.json", "docs/editorial/aula.wav", "modules/aula109.json.bak"]:
            self.assertFalse(allowed(path))

if __name__ == "__main__":
    unittest.main()
