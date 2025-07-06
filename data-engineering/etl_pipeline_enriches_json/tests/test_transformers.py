import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import src.transformers.address_transformer as at

def fake_geocode(addr, key):
    return {"full_address": "F", "latitude": "L", "longitude": "O"}

def test_transform_happy(monkeypatch):
    monkeypatch.setattr(at, "get_structured_address", fake_geocode)
    records = [{"project_address": "A"}, {"project_address": ""}]
    out = at.transform(iter(records), "key")
    # record[0] got F/L/O; record[1] got None, None, None
    assert out[0]["full_address"] == "F"
    assert out[0]["latitude"]    == "L"
    assert out[1]["full_address"] is None
    assert out[1]["latitude"]     is None