# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:37:11 2023

@author: Zara
"""

import matplotlib.pyplot as plt
import os as os
import pandas as pd

# Replace 'your_file_path.csv' with the actual path to your CSV file
directory = 'H:/My Drive/School/LSRI/2023_ZaraZ/data/SNOTEL/SnowDepth/'
sites = [file for file in os.listdir(directory) if file.endswith(".csv")]
dataframes = []

for site in sites:
    print(site)
    file_path = os.path.join(directory, site)
    df = pd.read_csv(file_path, skiprows=2)
    df = df[['Date', 'SNWD.I-1 (in) ']]
    df.rename(columns={'SNWD.I-1 (in) ': 'Snow Depth'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Append the DataFrame for each site to the list
    dataframes.append(df)

# Concatenate all DataFrames into one large DataFrame
snowDepth = pd.concat(dataframes)
snowDepth.sort_index(inplace=True)

os.chdir("H:/My Drive/School/LSRI/2023_ZaraZ/data/SNOTEL/SnowDepth/")
snowDepth.to_pickle('MartenRidge_SnowDepth_2018-2023.pkl')

plt.figure()
plt.scatter(snowDepth.index, snowDepth['Snow Depth'])
plt.xlabel('Date')
plt.ylabel('Snow Depth (inches)')
plt.ylim(0,200)
plt.title('Marten Ridge Snow Depth, 2018-2023')
plt.grid(True)
plt.show()