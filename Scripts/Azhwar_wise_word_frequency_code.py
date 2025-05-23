#!/usr/bin/env python3
# Authors: Dinesh M, 
#          Ragothaman M. Yennamalli, SASTRA Deemed to be University
# Last Modified: 2024-10-23
# Description:
#   This Python script counts the frequency of unique words in the first sections (before "–") of .txt files within a specified folder, 
#   cleaning punctuation and filtering empty entries. The word frequencies are saved as a CSV file for analysis.

import os
import pandas as pd
from collections import Counter

def word_count_in_corpus(folder_path, output_csv):
    word_counter = Counter()

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            
            print(f"Processing file: {file_name}...")
            
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    first_part = line.split('–')[0]
                    
                    words = first_part.split()

                    words = [word.strip("!@#$%^&*()-_=+:;<>?,.'’/[]") for word in words]

                    words = [x for x in words if x]
                    
                    word_counter.update(words)

    word_df = pd.DataFrame(word_counter.items(), columns=['Word', 'Count'])
    
    word_df.to_csv(output_csv, index=False)
    
    print(f"Word count saved to {output_csv}")

azhwar = "phrases"
folder_path = f"path_to_your_directory"  
output_csv = f"path_to_your_directory"        

word_count_in_corpus(folder_path, output_csv) 

