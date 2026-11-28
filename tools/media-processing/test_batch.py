import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import batch

class BatchTests(unittest.TestCase):
    def test_resume_failure_duplicate_and_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root/"in"
            src.mkdir()
            dest = root/"out"
            (src/"a.wav").write_bytes(b"one")
            (src/"b.wav").write_bytes(b"two")
            (src/"c.wav").write_bytes(b"one")
            (src/"bad.wav").write_bytes(b"bad")
            model_instance = object()
            calls = []
            def recognize(path, model, model_dir, engine=None):
                if path.read_bytes() == b"bad":
                    raise ValueError("Synthetic failure")
                calls.append(engine)
                return {"model":model,"language":"pt","segments":[{"start":0,"end":1.5,"text":"teste"}]}, model_instance
            self.assertEqual(batch.process(src,dest,recognizer=recognize),{"processed":2,"skipped":1,"failed":1})
            self.assertEqual(calls,[None,model_instance])
            self.assertEqual(batch.process(src,dest,recognizer=recognize),{"processed":0,"skipped":3,"failed":1})
            (src/"a.wav").write_bytes(b"changed")
            self.assertEqual(batch.process(src,dest,recognizer=recognize),{"processed":1,"skipped":2,"failed":1})
            for folder in dest.iterdir():
                self.assertEqual(set(p.name for p in folder.iterdir()),{"manifest.json","transcript.json","transcript.txt","transcript.srt"})
                self.assertIn("00:00:00,000 --> 00:00:01,500",(folder/"transcript.srt").read_text())
                self.assertEqual((folder/"transcript.json").stat().st_mode & 0o777,0o600)
            # A corrupted export must never be counted as complete or overwritten.
            folder = next(dest.iterdir())
            (folder/"transcript.txt").write_text("corrupted")
            result = batch.process(src,dest,recognizer=recognize)
            self.assertGreaterEqual(result["failed"],2)

    def test_ci_disabled(self):
        with patch.dict(os.environ,{"GITHUB_ACTIONS":"true"}),patch("sys.argv",["batch","input","output"]),patch("batch.process") as process:
            self.assertEqual(batch.main(),1)
            process.assert_not_called()

    def test_overlap_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                batch.process(tmp,Path(tmp)/"output")

    def test_timestamp_rounding(self):
        self.assertEqual(batch.timestamp(3599.9996),"01:00:00,000")

if __name__ == "__main__":
    unittest.main()
