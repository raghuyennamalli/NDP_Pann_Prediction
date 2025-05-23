#!/usr/bin/env python3
# Authors: Dinesh M, 
#          Ragothaman M. Yennamalli, SASTRA Deemed to be University
# Last Modified: 2024-10-22
# Description:
#   This Python script calculates the word count for specific sections (before "–") in all .txt files 
#   within a specified folder and compiles the results into a DataFrame. 
#   It saves the aggregated word counts as a CSV file for further analysis.

import os
import pandas as pd

def count_words_in_txt_files(folder_path):
    data = []
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                word_count = 0
                
                for line in file:
                    first_part = line.split("–")[0].strip()
                
                    word_count += len(first_part.split())
            
            data.append({'file_name': file_name, 'count': word_count})
    
    df = pd.DataFrame(data)
    
    output_path = os.path.join("..\\", f"{folder_path}_word_count.csv")
    df.to_csv(output_path, index=False)
    
    return df

folder_path = "path_to_your_directory"
word_count_df = count_words_in_txt_files(folder_path)
print(word_count_df)

