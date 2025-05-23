#!/usr/bin/env python3
# Authors: Dinesh M, 
#          Ragothaman M. Yennamalli, SASTRA Deemed to be University
# Last Modified: 2024-10-22
# Description:
#   This Python script counts the number of lines or hyphen-separated sections in .txt files within a specified directory, 
#   recording the minimum of these counts for each file. The results are saved to a CSV file for analysis, 
#   with a detailed progress display during execution.

import os
import pandas as pd

def line_counter(directory_path, output_file):
    data = []
    
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory_path, file_name)
            
            print(f"Processing file: {file_name}...")
            
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                content = content.strip("\n")
                line_count = content.count("\n") + 1
                hyphen_count = content.count("–")
                count = min(hyphen_count, line_count)
            
            data.append([file_name, count])
            
            print(f"Found {count} lines in {file_name}")
    
    df = pd.DataFrame(data, columns=["File Name", "Count"])

    df.to_csv(output_file, index=False)
    
    print(f"DataFrame saved to {output_file}")
    print(df)

azhwar = "Poigai Azhwar"
directory_path = f"path_to_your_directory"
output_file = f"path_to_your_directory"
line_counter(directory_path, output_file)
