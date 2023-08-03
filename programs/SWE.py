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
    df = df[['Date', 'WTEQ.I-1 (in) ']]
    df.rename(columns={'WTEQ.I-1 (in) ': 'SWE'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Append the DataFrame for each site to the list
    dataframes.append(df)

# Concatenate all DataFrames into one large DataFrame
SWE = pd.concat(dataframes)
SWE.sort_index(inplace=True)
print(SWE)

os.chdir("H:/My Drive/School/LSRI/2023_ZaraZ/data/SnowDensity/")
SWE.to_pickle('MartenRidge_SWE_2018-2023.pkl')

plt.figure()
plt.scatter(SWE.index, SWE['SWE'])
plt.xlabel('Date')
plt.ylabel('Snow Water Equivalent (inches)')
plt.ylim(0,100)
plt.title('Marten Ridge SWE, 2018-2023')
plt.grid(True)
plt.show()