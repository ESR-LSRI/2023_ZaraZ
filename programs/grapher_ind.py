# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:16:25 2023

@author: Zara
"""

#import numpy as np
import matplotlib.pyplot as plt
import os as os
import pickle
import matplotlib.patches as mpatches

# IMPORTANT: FILES ARE STRUCTURED DIFFERENTLY

directory = 'G:/My Drive/School/LSRI/2023_ZaraZ/data/pkl/'
#site = input("Site: ")
#directory = path + site + ".pkl"

folder_elevation = {
    "1_buried": 1066,
    "2_buried": 1179,
    "3_buried": 1349,
    "4_buried": 1475,
    "5west_buried": 1692,
    "6_buried": 1792,
    "7_buried": 2065,
}

year_color = {
    "2018-2019": '#BCD2E8',
    "2019-2020": '#91BAD6',
    "2020-2021": '#73A5C6',
    "2021-2022": '#528AAE',
    "2022-2023": '#2E5984',
}


plt.figure()
plt.title('Snow Cover Duration by Elevation, 2018-2023', fontsize=18)
plt.xlabel('# of days with snow cover', fontsize=15)
plt.ylabel('Elevation (m)', fontsize=15)
plt.xlim(0, 365)
plt.ylim(800, 2200)

legend_handles = [mpatches.Patch(color=color, label=year) for year, color in year_color.items()]

plt.legend(handles=legend_handles, loc='upper left', title='Year')
#plt.grid(True)

# Loop through the main directory to find folders containing 'buried'
for folder in os.listdir(directory):
    if folder in folder_elevation:
        folder_path = os.path.join(directory, folder)
        elevation = folder_elevation[folder]
        
        for file in os.listdir(folder_path):
            if file.endswith('.pkl'):
                file_path = os.path.join(folder_path, file)
                
                with open(file_path, 'rb') as f:
                    # Load the .pkl file into a DataFrame and append to the list
                    df = pickle.load(f)
                    daily_mean_temp = df.resample('D').mean()
                    daily_std_temp = df.resample('D').std()
                    snow_cover = (
                        (daily_mean_temp['Value'] >= -1) & 
                        (daily_mean_temp['Value'] <= 1) & 
                        (daily_std_temp['Value'] < 0.45)
                    )
                    
                    snow_covered_dates = snow_cover.index[snow_cover]
                    
                    for year in year_color.keys():
                        if year in file:
                            color = year_color[year]
                            break 
                    #elevation_plot = [elevation] * len(snow_cover.index)
                    plt.scatter(len(snow_covered_dates), elevation, color = color)

# colNames = [c[:-4] for f in fileNames]
#os.chdir(fileLoc)
#plt.title(site)


'''for site in sites:
    file_path = os.path.join(directory, site)
    with open(file_path, 'rb') as f:
        #print(elevation)
        df = pickle.load(f)
        snow_cover = df[(df['Value'] >= -1) & (df['Value'] <= 1)] # change snow cover condition here
        elevation = int(site[-8:-4]) # gets elevation from file name 
        elevation_plot = [elevation] * len(snow_cover.index)
        #print(snow_cover.index)
        plt.scatter(snow_cover.index, elevation_plot, color = "mediumslateblue")'''

#print(df)    

# plot the temperature  time series


