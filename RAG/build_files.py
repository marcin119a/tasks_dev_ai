import pandas as pd
import os
from dotenv import load_dotenv

# 1. Define the output folder
load_dotenv()
output_folder = os.getenv("OUTPUT_FOLDER", "adresowo_descriptions")

# 2. Check if the folder already exists
print("Downloading data and generating text files...")

# 3. Download the data
df = pd.read_csv("https://raw.githubusercontent.com/marcin119a/data/refs/heads/main/adresowo_offers_detail.csv")

# 4. Create the folder
os.makedirs(output_folder, exist_ok=True)

# 5. Save descriptions to individual .txt files
for index, row in df.head(12).iterrows():
    desc = row.get("description")
    if pd.notna(desc):
        with open(f"{output_folder}/desc_{index}.txt", "w", encoding="utf-8") as f:
            f.write(str(desc))

print(f"Descriptions saved to '{output_folder}'")
