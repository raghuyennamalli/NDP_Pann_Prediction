#!/usr/bin/env python3
# Authors: Dinesh M, 
#          Ragothaman M. Yennamalli, SASTRA Deemed to be University
# Last Modified: 2025-04-30
# Description:
#   This script parses a Tamil text file to extract songs and their associated Pann, 
#   filtering unwanted lines and validating song length. It then cleans the text to retain only Tamil characters and exports 
#   the structured data to an Excel file.


import re
import pandas as pd

input_file = "path_to_your_directory"  

with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

songs = []
current_pann = None
song_data = []
current_song = []
song_line_count = 0

pann_pattern = re.compile(r"பண்\s*-\s*(.*)௿")  
number_pattern = re.compile(r"^\d+") 
remove_extras = ["திருச்சிற்றம்பலம்", "இத்தலம்", "சுவாமிபெயர்"]  

for line in lines:
    line = line.strip()

    if any(extra in line for extra in remove_extras):
        continue

    pann_match = pann_pattern.match(line)
    if pann_match:
        current_pann = pann_match.group(1).strip()
        continue 

    if number_pattern.match(line):
        if current_song and song_line_count in [4, 6]:  
            song_data.append({"Song": "\n".join(current_song), "PANN": current_pann})
        current_song = []  
        song_line_count = 0  
        line = number_pattern.sub("", line).strip()  

    if line:
        current_song.append(line)
        song_line_count += 1


if current_song and song_line_count in [4, 6]:
    song_data.append({"Song": "\n".join(current_song), "PANN": current_pann})

df = pd.DataFrame(song_data)

def clean_song_text(song):
    song = str(song).strip()  
    return "".join(re.findall(r"[\u0B80-\u0BFF\s]", song)) 

df["Song"] = df["Song"].apply(clean_song_text)

output_file = "path_to_your_directory"
df.to_excel(output_file, index=False)

print(f" Processing complete! Cleaned file saved as {output_file}")
