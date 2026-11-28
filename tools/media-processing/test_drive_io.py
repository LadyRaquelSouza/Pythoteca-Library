import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import drive_io
from batch import process

class Fake:
    def __init__(self):
        self.data={"private:input/a.wav":b"synthetic","private:input/b.wav":b"synthetic"}
        self.uploads=[]
    def check_drive(self,remote):
        assert remote=="private"
    def list(self,remote):
        return [{"Path":k[len(remote)+1:]} for k in self.data if k.startswith(remote+"/")]
    def download(self,source,local):
        local.write_bytes(self.data[source])
    def upload(self,local,dest):
        assert dest not in self.data
        self.data[dest]=local.read_bytes()
        self.uploads.append(dest)

def processor(source,dest,model,model_dir):
    def recognize(path,model,model_dir,engine=None):
        return {"model":model,"language":"pt","segments":[{"start":0,"end":1,"text":"teste sintético"}]},object()
    return process(source,dest,model,model_dir,recognizer=recognize)

class DriveTests(unittest.TestCase):
    def test_dry_run_and_resume(self):
        client=Fake()
        args=("private:input","private:output",client)
        self.assertEqual(drive_io.sync(*args)["discovered"],2)
        self.assertEqual(client.uploads,[])
        first=drive_io.sync(*args,dry_run=False,processor=processor)
        self.assertEqual((first["processed"],first["skipped"],first["uploaded"],first["failed"]),(1,1,4,0))
        self.assertTrue(client.uploads[-1].endswith("/manifest.json"))
        second=drive_io.sync(*args,dry_run=False,processor=processor)
        self.assertEqual((second["processed"],second["skipped"],second["uploaded"],second["failed"]),(0,2,0,0))

    def test_paths(self):
        for a,b in [("private:input","private:input/output"),("private:input","other:output"),("private:","private:output")]:
            with self.assertRaises(ValueError):
                drive_io.validate_pair(a,b)
        for path in ["../a.wav","/a.wav","a/../b.wav","a//b.wav"]:
            with self.assertRaises(ValueError):
                drive_io.safe_relative(path)

    def test_ci_block(self):
        with patch.dict(os.environ,{"GITHUB_ACTIONS":"true"}),patch("sys.argv",["drive_io","--source","private:input","--destination","private:output","--config","fake"]),patch("drive_io.Rclone") as client:
            self.assertEqual(drive_io.main(),1)
            client.assert_not_called()

if __name__=="__main__":
    unittest.main()
