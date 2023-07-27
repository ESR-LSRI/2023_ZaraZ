# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:22:28 2023

@author: Zara
"""

# import
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

directory = "G:/My Drive/School/LSRI/2023_ZaraZ/data/SNOTEL/Marten_Ridge_snowwater.csv"
unneeded_columns = ["Min","10%","30%","70%","90%","Max","Median ('91-'20)","Median (POR)","Median Peak SWE"]
unneeded_columns_set = set(unneeded_columns)

df = pd.read_csv(directory)

columns_to_keep = [col for col in df.columns if col not in unneeded_columns_set]

# Create a new DataFrame with the desired columns
df = df[columns_to_keep]
df.drop(columns=['2023'], inplace=True)
df.set_index('date', inplace=True)

# Calculate snowdays and snowamount for each column
snowdays = (df != 0).sum()  # Count non-zero values for each column
snowamount = df[df != 0].sum()  # Sum non-zero values for each column

# Create a DataFrame with snowdays and snowamount as columns
snow_data = pd.DataFrame({'snowdays': snowdays, 'snowamount': snowamount})
slope, intercept = np.polyfit(snow_data['snowdays'], snow_data['snowamount'], 1)

plt.figure()
# Plot snowdays on the x-axis and snowamount on the y-axis
plt.scatter(snow_data['snowdays'], snow_data['snowamount'])
plt.plot(snow_data['snowdays'], slope * snow_data['snowdays'] + intercept, color='black', label='Trendline')
for col_name, x, y in zip(snow_data.index, snow_data['snowdays'], snow_data['snowamount']):
    plt.annotate(col_name, (x, y), textcoords="offset points", xytext=(5,5), ha='center')
    
plt.xlabel('# of snow days')
plt.xlim(0, 365)
plt.ylabel('total snow water equivalent (in.)')
plt.ylim(0, 13000)
plt.title('Snow Days vs. Snow Amount')
plt.show()