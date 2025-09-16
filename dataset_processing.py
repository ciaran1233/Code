import csv
import json
import xml.etree.ElementTree as et
from pathlib import Path
import pandas as pd

# Define my dataset

dataset = [
    {"id": 1, "name": "alice", "email": "alice@example.com", "age": 30},
    {"id": 2, "name": "bob", "email": "bob@example.com", "age": 26},
    {"id": 3, "name": "jerry", "email": "jerry@example.com", "age": 28}
]

# Create output folder
output_folder = Path("data_formats")
output_folder.mkdir(exist_ok=True)

# Convert to DataFrame

df = pd.DataFrame(dataset)

# Convert to CSV
csv_file = output_folder / "dataset.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=dataset[0].keys())
    writer.writeheader()
    writer.writerows(dataset)

# Convert to JSON
json_file = output_folder / "dataset.json"
df.to_json(json_file, orient='records')
