# -*- coding: utf-8 -*-
"""
Program cleans and re-structures data from iButton csv files
and saves dataframes in a .pkl (pickle) file

@author: Zara
"""

# imports
import os
import csv
import pandas as pd

# directory location
directory = "" # insert directory containing csv data files here
os.chdir("") # insert directory for saving pkl files here

# Get all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

# Bad characters list (specific to 2022-2023)
bad_chars = ['â', '€', '¯', '']

# Loop through each CSV file
for file_name in csv_files:
    file_path = os.path.join(directory, file_name)
    
    # opens file
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = list(csv_reader)
        
        # checks number of columns (most have 3, some have 4)
        if len(lines) >= 16:
            num_columns = len(lines[15]) # Line numbers are 0-based
            df = pd.read_csv(file_path, encoding="unicode_escape", skiprows=14) # converts to dataframe
            
            if num_columns == 3:
                
                # create datetime variable, set as index
                df['datetime'] = pd.to_datetime(df['Date/Time'], errors = "coerce")
                df = df.set_index('datetime')

                # drop useless columns
                df.drop(['Unit','Date/Time'],axis = 'columns',inplace = True)
                
                # just for visual confirmation
                print(file_name)
                print(df)
            else:
                
                # reset index
                df.reset_index(inplace=True)
                
                # replace with correct indices
                columnsOld = df.columns.append(pd.Index(["Temp"]))
                columnsNew = ["Date", "ts", "Unit", "Value"]
                dictColumns = dict(zip(columnsOld, columnsNew))
                df = df.rename(columns = dictColumns)
                
                # checks for bad characters in "ts" (time) column
                # (specific to 2022-2023 data so far)
                bad_char_occurrences = df["ts"].apply(lambda x: any(char in x for char in bad_chars))
                
                if bad_char_occurrences.any():
                    df["ts"] = df["ts"].apply(lambda x: ''.join(char for char in x if char not in bad_chars))
            
                # combine the columns
                df['Date/Time'] = df['Date'] + df['ts']
            
                # convert "Date/Time" to datetime format
                df['datetime'] = pd.to_datetime(df['Date/Time'], errors = "coerce")
                df = df.set_index('datetime')
            
                # drop unnecessary columns
                df.drop(['Unit','Date', 'ts', 'Date/Time'],axis = 'columns',inplace = True)
                
                # just for visual confirmation
                print(file_name)
                print(df)
            
            # saves dataframe as pickle file to os.chdir() location set above
            df.to_pickle(file_name[:-3] + "pkl")
