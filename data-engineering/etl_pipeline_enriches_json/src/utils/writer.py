import json
import os
from typing import Iterator, Dict

def write_enriched_data(data_iter: Iterator[Dict], output_path: str):
    """
    Writes an iterator of dicts to a JSON file.
    Args:
        data_iter (iterable): An iterator of dictionaries to write to the JSON file.
        output_path (str): The file path where the JSON data will be written.
    """
    os.makedirs(output_path, exist_ok=True)
    out_file = os.path.join(output_path, "output.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(list(data_iter), f, indent=2, ensure_ascii=False)
    print(f"[writer] wrote {out_file}")
