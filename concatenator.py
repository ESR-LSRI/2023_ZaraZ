# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:05:54 2023

@author: Zara
"""

# imports
import pickle
import pandas as pd
import os as os

path = "G:/My Drive/School/LSRI/2023_ZaraZ/data/pkl/" # add data file path here
site = input("Site: ")
directory = path + site
pkl_files = [file for file in os.listdir(directory) if file.endswith(".pkl")]

data = []

# loop through files in site directory
for file in pkl_files:
    file_path = os.path.join(directory, file)
    with open(file_path, 'rb') as f:
        df = pickle.load(f)  
        #print(df.index.dtype)
        data.append(df)

        # Concatenate all dataframes into one
        frame = pd.concat(data)
        frame.sort_index(inplace=True)
        
os.chdir("G:/My Drive/School/LSRI/2023_ZaraZ/data/concatenated")
frame_name = site + '.pkl'
frame.to_pickle(frame_name) # save as .pkl (pickle) file

print(frame) # for visual confirmation'''