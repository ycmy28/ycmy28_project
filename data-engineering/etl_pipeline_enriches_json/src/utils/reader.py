import json
import os
from typing import Iterator, Dict

def read_json(folder_path: str) -> Iterator[Dict]:
    """
    Reads JSON files from a specified directory and yields each record.
    Args:
        folder_path (str): The directory containing JSON files.
    Yields:
        dict: Each record from the JSON files.
    """
    file_path = os.path.join(folder_path, "input_sample.json")
    with open(file_path, "r", encoding="utf-8") as f:
        for rec in json.load(f):
            yield rec
