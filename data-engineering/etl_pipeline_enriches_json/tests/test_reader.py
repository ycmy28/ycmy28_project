import os, sys, json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.utils.reader import read_json

def test_read(tmp_path):
    folder = tmp_path / "inp"
    folder.mkdir()
    data = [{"a":1}, {"b":2}]
    (folder / "input_sample.json").write_text(json.dumps(data))
    recs = list(read_json(str(folder)))
    assert recs == data

def test_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        list(read_json(str(tmp_path / "nope")))
