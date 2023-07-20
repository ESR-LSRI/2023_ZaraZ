# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:16:25 2023

@author: Zara
"""

#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os as os
import pickle

# IMPORTANT: FILES ARE STRUCTURED DIFFERENTLY

path = 'G:/My Drive/School/LSRI/2023_ZaraZ/data/concatenated/'
site = input("Site: ")
directory = path + site + ".pkl"

# colNames = [c[:-4] for f in fileNames]
#os.chdir(fileLoc)

with open(directory, 'rb') as f:
    df = pickle.load(f)     
print(df)    

# plot the temperature  time series
plt.figure()
plt.plot(df.index,df.Value)
plt.title(site)
plt.xlabel('Time')
plt.ylabel('Value')

#plt.figure()
#plt.plot(df)
