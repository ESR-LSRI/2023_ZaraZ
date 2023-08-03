# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 12:30:40 2023

@author: Zara
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'directory' with the actual directory path containing the .pkl files
directory = 'G:/My Drive/School/LSRI/2023_ZaraZ/data/SnowDensity/'

# Get a list of .pkl files in the directory
pkl_files = [file for file in os.listdir(directory) if file.endswith(".pkl")]
# Create an empty list to store DataFrames for each file
dataframes = []

# Read and concatenate all .pkl files
for file in pkl_files:
    file_path = os.path.join(directory, file)
    df = pd.read_pickle(file_path)
    dataframes.append(df)

# Concatenate the DataFrames by their indices
SnowDensity = pd.concat(dataframes, axis=1)
SnowDensity.loc[SnowDensity['Snow Depth'] < 12, 'Snow Depth'] = pd.NA
SnowDensity.loc[SnowDensity['SWE'] < 12, 'SWE'] = pd.NA

# Divide the values in the "SWE" column by the "Snow Depth" column
SnowDensity['Snow Density'] = SnowDensity['SWE'] / SnowDensity['Snow Depth']

print(SnowDensity)

plt.figure()
plt.plot(SnowDensity.index, SnowDensity['Snow Density'] * 997)
plt.xlabel('Date')
plt.ylabel('Snow Density (kg/m^3)')
plt.ylim(0,1000)
plt.title('Marten Ridge Snow Density, 2018-2023')
plt.show()