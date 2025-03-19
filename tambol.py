# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:05:22 2024

@author: Wasinn_1800
"""

import re

if __name__ == "__main__":
    
    with open('tambol.sql', 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    tMem = []
    for line in data:
        if "VALUES" in line:
            start = line.index(' (')
            end = line.index(');')
            values = line[start:end].split(', ')
    
            tcode = values[0].strip(' (')
            tname = values[1].strip("'")
            tCN = f'{tcode} {tname}'
                
            tMem.append(tCN)
                
    with open('outputT.txt', 'w', encoding='utf-8') as output_file:
        for i in tMem:
            output_file.write(f"{i}\n")
