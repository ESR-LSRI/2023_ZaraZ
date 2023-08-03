"""
PROGRAM TO CREATE A TIME SERIES GRAPH OF SNOW COVER
_________________________________________________________________________

At the time of writing this code, my data files were organized by site,
and all were in a single folder. Example:
    /data
        /snow cover graph
            /1_buried.pkl
            /2_buried.pkl
            ...
So this code is adapted specifically to this format and graphs by 
looping through the folder.
_________________________________________________________________________

@author: Zara Z. '24
"""

import matplotlib.pyplot as plt
import os as os
import pickle

# Directory information
directory = "" # File path to iButton data folder
sites = [file for file in os.listdir(directory) if file.endswith(".pkl")]

plt.figure()
plt.title('Snow Cover Duration by Elevation, 2018-2023', fontsize=18)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Elevation (m)', fontsize=15)
plt.ylim(800, 2200)

for site in sites:
    file_path = os.path.join(directory, site)
    with open(file_path, 'rb') as f:
        #print(elevation)
        df = pickle.load(f)
        daily_mean_temp = df.resample('D').mean()
        daily_std_temp = df.resample('D').std()
        snow_cover = (
            (daily_mean_temp['Value'] >= -1) & 
            (daily_mean_temp['Value'] <= 1) & 
            (daily_std_temp['Value'] < 0.45)
        )
        elevation = int(site[-8:-4]) # gets elevation from file name 
        snow_covered_dates = snow_cover.index[snow_cover]

        # Create a list with the elevation for each snow-covered date
        elevation_plot = [elevation] * len(snow_covered_dates)

        # Plot the elevation against the snow-covered dates
        plt.scatter(snow_covered_dates, elevation_plot, color='#528AAE', s=3)

#print(df)    

# plot the temperature  time series


