# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:01:40 2023

@author: Zara
"""

import os
import csv
import pandas as pd

directory = "G:/My Drive/School/LSRI/2023_ZaraZ/data/restructure1"
os.chdir("G:/My Drive/School/LSRI/2023_ZaraZ/data/pkl")

# Get all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

# Loop through each CSV file
for file_name in csv_files:
    file_path = os.path.join(directory, file_name)
    
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = list(csv_reader)
        
        if len(lines) >= 16:
            num_columns = len(lines[15]) # Line numbers are 0-based
            df = pd.read_csv(file_path, encoding="unicode_escape", skiprows=14)
            
            if num_columns == 3:

                # create datetime variable, set as index
                df['datetime'] = pd.to_datetime(df['Date/Time'], errors = "coerce")
                df = df.set_index('datetime')

                # drop useless columns
                df.drop(['Unit','Date/Time'],axis = 'columns',inplace = True)
                print(file_name)
                print(df)
            else:
                df.reset_index(inplace=True)
                columnsOld = df.columns.append(pd.Index(["Temp"]))
                columnsNew = ["Date", "ts", "Unit", "Value"]
                dictColumns = dict(zip(columnsOld, columnsNew))
                df = df.rename(columns = dictColumns)
            
                # combine the columns
                df['Date/Time'] = df['Date'] + df['ts']
            
                # convert "Date/Time" to datetime format
                df['datetime'] = pd.to_datetime(df['Date/Time'], errors = "coerce")
                df = df.set_index('datetime')
            
                # drop unnecessary columns
                df.drop(['Unit','Date', 'ts', 'Date/Time'],axis = 'columns',inplace = True)
                print(file_name)
                print(df)
            df.to_pickle(file_name[:-3] + "pkl")


