import csv
from typing import List, Dict

def save_to_csv(data: List[Dict], filename: str) -> None:
    if not data:
        return
    fieldnames = list(data[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
