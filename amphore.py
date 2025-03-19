# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:57:44 2024

@author: Wasinn_1800
"""

import re

if __name__ == "__main__":
    
    with open('amphoe.sql', 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    aMem = []
    for line in data:
        if "VALUES" in line:
            start = line.index(' (')
            end = line.index(');')
            values = line[start:end].split(', ')
    
            acode = values[0].strip(' (')
            aname = values[1].strip("'")
            aCN = f'{acode} {aname}'
                
            aMem.append(aCN)
                
    with open('outputA.txt', 'w', encoding='utf-8') as output_file:
        for i in aMem:
            output_file.write(f"{i}\n")
