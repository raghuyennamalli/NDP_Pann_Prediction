#!/usr/bin/env python3
# Authors: Dinesh M, 
#          Ragothaman M. Yennamalli, SASTRA Deemed to be University
# Last Modified: 2024-10-24
# Description:
#   This script processes .txt files in a specified folder, counting the frequency of cleaned phrases within each file. 
#   For every file, it generates a separate CSV containing phrases and their counts in each twelve azhwar, saved in the same folder.

import os
import pandas as pd
from collections import Counter

def phrase_count_in_file(file_path, output_csv):
    phrase_counter = Counter()

    file_name = os.path.basename(file_path)
    print(f"Processing file: {file_name}...")

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            if line:
                cleaned_phrase = line.strip("!@#$%^&*()-_=+:;<>?,.'’/[]”")

                phrase_counter.update([cleaned_phrase])

    phrase_df = pd.DataFrame(phrase_counter.items(), columns=['Phrase', 'Count'])

    phrase_df.to_csv(output_csv, index=False)

    print(f"Phrase count saved to {output_csv}")

def process_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            output_csv = os.path.join(folder_path, f"{os.path.splitext(file_name)[0]}_phrase_frequency.csv")
            
            phrase_count_in_file(file_path, output_csv)

folder_path = "path_to_your_directory".strip()

if os.path.isdir(folder_path):
    process_folder(folder_path)
else:
    print(f"The folder path '{folder_path}' is not valid. Please try again.")

