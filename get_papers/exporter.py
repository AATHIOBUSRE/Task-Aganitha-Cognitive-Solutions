from typing import List, Dict
import csv
import sys

def export_results(data: List[Dict], filename: str = None) -> None:
    if not data:
        print("No results found.")
        return

    fieldnames = list(data[0].keys())

    if filename:
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Results saved to {filename}")
    else:
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
