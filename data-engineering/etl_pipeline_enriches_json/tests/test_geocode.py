import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import requests
from src.integrations.geocode_util import get_structured_address

class DummyResp:
    def __init__(self, data, error=False):
        self._data = data
        self._error = error

    def raise_for_status(self):
        if self._error:
            raise requests.HTTPError("fail")

    def json(self):
        return self._data

def test_success(monkeypatch):
    fake = [{"display_name": "X Y Z", "lat": "9.99", "lon": "1.11"}]
    monkeypatch.setattr(requests, "get", lambda *a, **k: DummyResp(fake))
    out = get_structured_address("foo", "key")
    assert out == {"full_address": "X Y Z", "latitude": "9.99", "longitude": "1.11"}

def test_api_error(monkeypatch):
    monkeypatch.setattr(requests, "get", lambda *a, **k: DummyResp(None, error=True))
    out = get_structured_address("foo", "key")
    assert out["full_address"] is None
    assert out["latitude"]  is None
    assert out["longitude"] is None

def test_empty_input():
    out = get_structured_address("", "key")
    assert out == {"full_address": None, "latitude": None, "longitude": None}
