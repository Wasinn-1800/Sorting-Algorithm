# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:46:54 2024

@author: Wasinn_1800
"""

import re

if __name__ == "__main__":
    
    with open('province.sql', 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    pMem = []
    for line in data:
        if "VALUES" in line:
            start = line.index(' (')
            end = line.index(');')
            values = line[start:end].split(', ')
    
            pcode = values[0].strip(' (')
            pname = values[1].strip("'")
            pCN = f'{pcode} {pname}'
                
            pMem.append(pCN)
                
    with open('outputP.txt', 'w', encoding='utf-8') as output_file:
        for i in pMem:
            output_file.write(f"{i}\n")

