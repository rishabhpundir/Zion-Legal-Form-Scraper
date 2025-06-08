# import os
# import json
# import re
# import pandas as pd

# # === Step 1: Paths and file loading ===
# json_path = "status.json"  # replace with your actual JSON filename if different
# zip_folder = "saved"

# # === Step 2: Load JSON and get ZIP filenames ===
# with open(json_path, "r") as f:
#     data = json.load(f)

# zip_files = [f for f in os.listdir(zip_folder) if f.endswith(".zip")]

# # === Step 3: Extract normalized names (only letters, lowercase) ===
# def normalize(name):
#     return re.sub(r'[^a-z]', '', name.lower())  # Remove everything but lowercase a-z

# # Extract just the alphabetical part of ZIP filenames
# zip_names_normalized = set(normalize(os.path.splitext(f)[0]) for f in zip_files)

# # === Step 4: Filter JSON entries ===
# filtered_data = [
#     entry for entry in data
#     if normalize(entry["name"]) not in zip_names_normalized
# ]

# # === Step 5: Save filtered JSON back ===
# with open(json_path, "w") as f:
#     json.dump(filtered_data, f, indent=4)

# print(f"Filtered JSON. {len(data) - len(filtered_data)} entries removed. {len(filtered_data)} entries remaining.")

import json

# === Step 1: Load the JSON file ===
json_path = "status_ copy.json"  # replace if needed
txt_output_path = "entries.txt"

with open(json_path, "r") as f:
    data = json.load(f)

# === Step 2: Write to TXT file ===
with open(txt_output_path, "w") as f:
    for entry in data:
        f.write(f"{entry['name']} - {entry['url']}\n")

print(f"Written {len(data)} entries to {txt_output_path}")

