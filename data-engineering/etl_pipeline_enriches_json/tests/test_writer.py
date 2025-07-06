import os, sys, json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.utils.writer import write_enriched_data

def test_write(tmp_path):
    out_dir = tmp_path / "out"
    data = [{"x":1}, {"y":2}]
    write_enriched_data(iter(data), str(out_dir))
    written = json.loads((out_dir / "output.json").read_text())
    assert written == data
