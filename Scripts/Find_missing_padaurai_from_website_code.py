#!/usr/bin/env python3
# Authors: Dinesh M, 
#          Ragothaman M. Yennamalli, SASTRA Deemed to be University
# Last Modified: 2024-10-22
# Description:
#     This Python script to identify the missing pazhurams in Nalayira Divya Prabandham.

import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

base_url = "https://www.dravidaveda.org/?p="
output_folder = "scraped_tables"
error_log_file = "error_urls.txt"  

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

failed_urls = []

def scrape_and_save_table(url, file_name):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        failed_urls.append(url) 
        return
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')

    if table is None:
        print(f"No table found on {url}")
        failed_urls.append(url) 
        return
    df = pd.read_html(StringIO(str(table)))[0]

    df = df.drop_duplicates()
    def remove_duplicates(row):
        unique_values = []
        for value in row:
            if value not in unique_values:
                unique_values.append(value)
        unique_values.extend([''] * (len(row) - len(unique_values)))
        return pd.Series(unique_values)
    df = df.apply(remove_duplicates, axis=1)

  
    file_path = os.path.join(output_folder, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        for index, row in df.iterrows():
            file.write('\t'.join(str(value) for value in row) + '\n')

    print(f"Table from {url} has been saved to {file_path}")

for i in range(1337, 5680):
    current_url = f"{base_url}{i}"
    file_name = f"table_data_{i}.txt"
    scrape_and_save_table(current_url, file_name)

if failed_urls:
    with open(error_log_file, 'w', encoding='utf-8') as error_file:
        for url in failed_urls:
            last_four_digits = url.split('=')[-1]
            error_file.write(last_four_digits + '\n')
    print(f"Failed URLs logged in {error_log_file}")
