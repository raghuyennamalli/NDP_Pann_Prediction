#!/usr/bin/env python3
# Authors: Dinesh M, 
#          Ragothaman M. Yennamalli, SASTRA Deemed to be University
# Last Modified: 2025-02-22
# Description:
#   Filtering unwanted lines and validating song length. It then cleans the text to retain only Tamil characters and 
#   exports the structured data to an Excel file.

import re

input_file = 'path_to_your_directory'
output_file = 'path_to_your_directory'

with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

cleaned_content = re.sub(r'[\(\),\-:;\/\?!\"\']|\b\d+\b|(?<=\w)\.', '', content)

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(cleaned_content)

print(f"The cleaned file has been saved to {output_file}.")
