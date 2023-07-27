# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:10:29 2023

@author: Zara
"""

import matplotlib.pyplot as plt
import os as os
import pickle

directory = 'G:/My Drive/School/LSRI/2023_ZaraZ/data/pkl/1_buried'
sites = [file for file in os.listdir(directory) if file.endswith(".pkl")]

for site in sites:
    file_path = os.path.join(directory, site)
    with open(file_path, 'rb') as f:
        df = pickle.load(f)
        print(site)
        daily_mean_temp = df.resample('D').mean()
        daily_std_temp = df.resample('D').std()
        
        # Step 2: Create a boolean mask for snowdays based on the conditions
        snowday_mask = (
            (daily_mean_temp['Value'] >= -1) & 
            (daily_mean_temp['Value'] <= 1) & 
            (daily_std_temp['Value'] < 0.45)
        )
        
        # Step 3: Use the boolean mask to count the number of snowdays
        num_snowdays = snowday_mask.sum()
        
        # Step 4: Print or use the result as needed
        print("Number of snowdays:", num_snowdays)
        print()