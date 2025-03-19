# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 22:14:46 2025

@author: Wasinn-1800
"""

import re

if __name__ == "__main__":
    
    with open('mm.sql', 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    mMem = []
    for line in data:
        if "VALUES" in line:
            start = line.index(' (')
            end = line.index(');')
            values = line[start:end].split(', ')
    
            mcode = values[0].strip(" ('")
            mname = values[1].strip("'")
            mCN = f'{mcode} {mname}'
                
            mMem.append(mCN)
                
    with open('outputM.txt', 'w', encoding='utf-8') as output_file:
        for i in mMem:
            output_file.write(f"{i}\n")
