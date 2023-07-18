# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:38:16 2023

@author: Zara
"""

import os
import pandas as pd

# returns list of files that have the wrong format
def findFiles(dir):
    r = []
    
    # loop through files in /restructure
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            df = pd.read_csv(file_path, encoding="unicode_escape", header=14)
            
            # detect files with 4 columns instead of 3
            if len(df.axes[1]) == 4:
                r.append(df)
    return r

directory = 'G:/My Drive/School/LSRI/2023_ZaraZ/data/restructure'
toRestructure = findFiles(directory)
os.chdir('G:/My Drive/School/LSRI/2023_ZaraZ/data/restructure')

# rename the columns
for file in toRestructure:
    columnsOld = file.columns
    columnsNew = ["Date", "ts", "Unit", "Value"]
    dictColumns = dict(zip(columnsOld, columnsNew))
    file = file.rename(columns = dictColumns)

    # combine the columns
    file['Date/Time'] = file['Date'] + file['ts']

    # convert "Date/Time" to datetime format
    file['datetime'] = pd.to_datetime(file['Date/Time'])
    file = file.set_index('datetime')

    # drop unnecessary columns
    file.drop(['Unit','Date', 'ts', 'Date/Time'],axis = 'columns',inplace = True)
    print(file)