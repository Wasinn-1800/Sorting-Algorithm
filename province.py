# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 21:47:29 2025

@author: Wasinn-1800
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

