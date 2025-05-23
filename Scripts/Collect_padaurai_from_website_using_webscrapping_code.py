#!/usr/bin/env python3
# Authors: Dinesh M, 
#          Ragothaman M. Yennamalli, SASTRA Deemed to be University
# Last Modified: 2024-9-4
# Description:
#   This Python script scrapes tables from specified URLs on the www.dravidaveda.org website, 
#   cleans the data by removing duplicates, and saves it as text files in a specified folder. 

import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO


base_url = "https://www.dravidaveda.org/?p="
output_folder = "scraped_tables_missing"
error_log_file = "error_urls.txt"  
empty_table_log_file = "empty_tables.txt"  

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

  
    if (df == '').sum().sum() > 0:
        with open(empty_table_log_file, 'a', encoding='utf-8') as fl:
            fl.write(url[-4:] + '\n')

   
    file_path = os.path.join(output_folder, file_name)
    

    with open(file_path, 'w', encoding='utf-8') as file:
        for index, row in df.iterrows():
     
            cleaned_row = ''.join([str(value).strip() for value in row])

            file.write(cleaned_row + '\n') 

    print(f"Table from {url} has been saved to {file_path}")


missed = [5681,5682,5683,5684,5685,5686,5687,5688,5689,15768,5690,5691,5692,
          5693,5694,5695,5696,5697,5698,5699,5700,5701,5702,5703,5704,5705,5706,
          5707,5708,5709,5710,5711,5712,5713,5714,5715,5716,5717,5718,5719,5720,5721]
for i in missed:  
    current_url = f"{base_url}{i}"
    file_name = f"table_data_{i}.txt"
    scrape_and_save_table(current_url, file_name)


if failed_urls:
    with open(error_log_file, 'w', encoding='utf-8') as error_file:
        for url in failed_urls:
            last_four_digits = url.split('=')[-1]
            error_file.write(last_four_digits + '\n')
    print(f"Failed URLs logged in {error_log_file}") 
 

