#!/usr/bin/env python3
# Authors: Dinesh M, 
#          Ragothaman M. Yennamalli, SASTRA Deemed to be University
# Last Modified: 2024-10-15
# Description:
#   This Python script calculates the frequency of Tamil words starting with "Uyir ezhuttukkal" (vowel letters) across multiple text files 
#   in subfolders of a main directory. The results are aggregated into a single CSV file, summarizing counts for each folder.
import os
import pandas as pd
from tamil import utf8


def starts_with_uyir_eluttukkal(word):
    if not word:  
        return False
    uyir_eluttukkal = utf8.uyir_letters  
    return word[0] in uyir_eluttukkal

def count_words_starting_with_uyir_in_file(file_path):
    uyir_eluttukkal = utf8.uyir_letters
    counts = {uyir: 0 for uyir in uyir_eluttukkal}  

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
           
            text_before_hyphen = line.split('-')[0]
            words = utf8.get_words(text_before_hyphen)
            for word in words:
                if starts_with_uyir_eluttukkal(word): 
                    first_letter = word[0]
                    counts[first_letter] += 1  

    return counts

def count_words_starting_with_uyir_in_folder(folder_path):
    uyir_eluttukkal = utf8.uyir_letters  
    folder_counts = {uyir: 0 for uyir in uyir_eluttukkal}  
   
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            file_counts = count_words_starting_with_uyir_in_file(file_path)  
            
            for uyir, count in file_counts.items():
                folder_counts[uyir] += count

    return folder_counts

def process_all_subfolders_to_single_csv(main_folder_path):
    uyir_eluttukkal = utf8.uyir_letters  
    overall_data = []  
    
    
    for folder_name in os.listdir(main_folder_path):
        subfolder_path = os.path.join(main_folder_path, folder_name)
        

        if os.path.isdir(subfolder_path):
            print(f"Processing folder: {subfolder_path}")
            folder_counts = count_words_starting_with_uyir_in_folder(subfolder_path)
            
           
            folder_data = [folder_name] + [folder_counts[uyir] for uyir in uyir_eluttukkal]
            overall_data.append(folder_data)
    
   
    columns = ['Folder'] + list(uyir_eluttukkal)  
    df = pd.DataFrame(overall_data, columns=columns)
    
   
    output_csv = os.path.join(main_folder_path, 'path_to_your_directory')
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"Single CSV file saved at: {output_csv}")

main_folder_path = 'path_to_your_directory'
process_all_subfolders_to_single_csv(main_folder_path)


