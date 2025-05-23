#!/usr/bin/env python3
# Authors: Dinesh M, 
#          Ragothaman M. Yennamalli, SASTRA Deemed to be University
# Last Modified: 2024-10-22
# Description:
#   This Python script analyzes text files within subfolders to count occurrences of Tamil words starting with specific "Uyirmei ezhuttukkal" (vowel-consonant). 
#   The results are aggregated into a single CSV file summarizing the counts for each subfolder.
import os
import pandas as pd
from collections import defaultdict
from tamil import utf8

uyirmei_groups = {
    'க்': ['க', 'கா', 'கி', 'கீ', 'கு', 'கூ', 'கெ', 'கே', 'கை', 'கொ', 'கோ', 'கௌ'],
    'ங்': ['ங', 'ஙா', 'ஙி', 'ஙீ', 'ஙு', 'ஙூ', 'ஙெ', 'ஙே', 'ஙை', 'ஙொ', 'ஙோ', 'ஙௌ'],
    'ச்': ['ச', 'சா', 'சி', 'சீ', 'சு', 'சூ', 'செ', 'சே', 'சை', 'சொ', 'சோ', 'சௌ'],
    'ஞ்': ['ஞ', 'ஞா', 'ஞி', 'ஞீ', 'ஞு', 'ஞூ', 'ஞெ', 'ஞே', 'ஞை', 'ஞொ', 'ஞோ', 'ஞௌ'],
    'ட்': ['ட', 'டா', 'டி', 'டீ', 'டு', 'டூ', 'டெ', 'டே', 'டை', 'டொ', 'டோ', 'டௌ'],
    'ண்': ['ண', 'ணா', 'ணி', 'ணீ', 'ணு', 'ணூ', 'ணெ', 'ணே', 'ணை', 'ணொ', 'ணோ', 'ணௌ'],
    'த்': ['த', 'தா', 'தி', 'தீ', 'து', 'தூ', 'தெ', 'தே', 'தை', 'தொ', 'தோ', 'தௌ'],
    'ந்': ['ந', 'நா', 'நி', 'நீ', 'நு', 'நூ', 'நெ', 'நே', 'நை', 'நொ', 'நோ', 'நௌ'],
    'ப்': ['ப', 'பா', 'பி', 'பீ', 'பு', 'பூ', 'பெ', 'பே', 'பை', 'பொ', 'போ', 'பௌ'],
    'ம்': ['ம', 'மா', 'மி', 'மீ', 'மு', 'மூ', 'மெ', 'மே', 'மை', 'மொ', 'மோ', 'மௌ'],
    'ய்': ['ய', 'யா', 'யி', 'யீ', 'யு', 'யூ', 'யெ', 'யே', 'யை', 'யொ', 'யோ', 'யௌ'],
    'ர்': ['ர', 'ரா', 'ரி', 'ரீ', 'ரு', 'ரூ', 'ரெ', 'ரே', 'ரை', 'ரொ', 'ரோ', 'ரௌ'],
    'ல்': ['ல', 'லா', 'லி', 'லீ', 'லு', 'லூ', 'லெ', 'லே', 'லை', 'லொ', 'லோ', 'லௌ'],
    'வ்': ['வ', 'வா', 'வி', 'வீ', 'வு', 'வூ', 'வெ', 'வே', 'வை', 'வொ', 'வோ', 'வௌ'],
    'ழ்': ['ழ', 'ழா', 'ழி', 'ழீ', 'ழு', 'ழூ', 'ழெ', 'ழே', 'ழை', 'ழொ', 'ழோ', 'ழௌ'],
    'ள்': ['ள', 'ளா', 'ளி', 'ளீ', 'ளு', 'ளூ', 'ளெ', 'ளே', 'ளை', 'ளொ', 'ளோ', 'ளௌ'],
    'ற்': ['ற', 'றா', 'றி', 'றீ', 'று', 'றூ', 'றெ', 'றே', 'றை', 'றொ', 'றோ', 'றௌ'],
    'ன்': ['ன', 'னா', 'னி', 'னீ', 'னு', 'னூ', 'னெ', 'னே', 'னை', 'னொ', 'னோ', 'னௌ']
}

def count_uyirmei_words(folder_path):
    counts = defaultdict(int)
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                
                for word in content.split():
                    for uyirmei, letters in uyirmei_groups.items():
                        if word.startswith(tuple(letters)):
                            counts[uyirmei] += 1
                            break

    return counts

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
            uyirmei_counts = count_uyirmei_words(subfolder_path)
            uyir_counts = count_words_starting_with_uyir_in_folder(subfolder_path)
            
            folder_data = [folder_name] + [uyirmei_counts.get(uyirmei, 0) for uyirmei in uyirmei_groups.keys()] + [uyir_counts[uyir] for uyir in uyir_eluttukkal]
            overall_data.append(folder_data)
    
    columns = ['Folder'] + list(uyirmei_groups.keys()) + list(uyir_eluttukkal)  
    df = pd.DataFrame(overall_data, columns=columns)
    
    output_csv = os.path.join(main_folder_path, 'combined_word_counts_summary.csv')
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"Single CSV file saved at: {output_csv}")

main_folder_path = 'path_to_your_directory'
process_all_subfolders_to_single_csv(main_folder_path)