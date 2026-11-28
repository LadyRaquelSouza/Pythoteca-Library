import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import transcribe

class PrivacyTests(unittest.TestCase):
    def test_repository_rejected(self):
        with self.assertRaises(ValueError):
            transcribe.outside(transcribe.ROOT / "private.wav")

    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            link = Path(tmp)/"link"
            link.symlink_to(transcribe.ROOT, target_is_directory=True)
            with self.assertRaises(ValueError):
                transcribe.outside(link/"private.wav")

    def test_prepare(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp)/"synthetic.wav"
            source.touch()
            target = Path(tmp)/"result.json"
            self.assertEqual(transcribe.prepare(source,target), (source,target))
            target.touch()
            with self.assertRaises(ValueError):
                transcribe.prepare(source,target)

    def test_ci_disabled(self):
        with patch.dict("os.environ", {"GITHUB_ACTIONS":"true"}), patch("sys.argv", ["transcribe","synthetic.wav","result.json"]), patch("transcribe.run") as run:
            self.assertEqual(transcribe.main(),1)
            run.assert_not_called()

if __name__ == "__main__":
    unittest.main()
