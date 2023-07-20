# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:16:25 2023

@author: Zara
"""

#import numpy as np
import matplotlib.pyplot as plt
import os as os
import pickle

# IMPORTANT: FILES ARE STRUCTURED DIFFERENTLY

directory = 'G:/My Drive/School/LSRI/2023_ZaraZ/data/snow_cover/'
#site = input("Site: ")
#directory = path + site + ".pkl"
sites = [file for file in os.listdir(directory) if file.endswith(".pkl")]

# colNames = [c[:-4] for f in fileNames]
#os.chdir(fileLoc)
#plt.title(site)

plt.figure()
plt.title('Snow Cover Duration by Elevation, 2018-2023')
plt.xlabel('Year')
plt.ylabel('Elevation (m)')
plt.ylim(800, 2200)

for site in sites:
    file_path = os.path.join(directory, site)
    with open(file_path, 'rb') as f:
        #print(elevation)
        df = pickle.load(f)
        snow_cover = df[(df['Value'] >= -1) & (df['Value'] <= 1)] # change snow cover condition here
        elevation = int(site[-8:-4]) # gets elevation from file name 
        elevation_plot = [elevation] * len(snow_cover.index)
        #print(snow_cover.index)
        plt.scatter(snow_cover.index, elevation_plot, color = '#528AAE', s=2)

#print(df)    

# plot the temperature  time series


