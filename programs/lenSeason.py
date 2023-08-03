# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:22:28 2023

@author: Zara
"""

# import
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

directory = "H:/My Drive/School/LSRI/2023_ZaraZ/data/SNOTEL/Marten_Ridge_snowwater.csv"
unneeded_columns = ["Min","10%","30%","70%","90%","Max","Median ('91-'20)","Median (POR)","Median Peak SWE"]
unneeded_columns_set = set(unneeded_columns)

df = pd.read_csv(directory)

columns_to_keep = [col for col in df.columns if col not in unneeded_columns_set]

# Create a new DataFrame with the desired columns
df = df[columns_to_keep]
df.drop(columns=['2023'], inplace=True)
df.set_index('date', inplace=True)

maxAccumulation = df.max()
maxAccumulation_df = pd.DataFrame({'Max Accumulation': maxAccumulation})

firstDay = df.ne(0).idxmax()
lastDay = df.ne(0).iloc[::-1].idxmax()

firstDay_df = pd.DataFrame({'First Day': firstDay})
lastDay_df = pd.DataFrame({'Last Day': lastDay})

# Join the two DataFrames based on their indices (column names)
seasonRange = pd.concat([firstDay_df, lastDay_df], axis=1)

for i, row in seasonRange.iterrows():
    row['First Day'] = row['First Day'] + '-' + str(int(i)-1)
    row['Last Day'] = row['Last Day'] + '-' + i
    
seasonRange = seasonRange.apply(pd.to_datetime)
seasonRange['Length'] = (seasonRange['Last Day'] - seasonRange['First Day']).dt.days + 1

plot = pd.concat([maxAccumulation_df, seasonRange['Length']], axis=1)
slope, intercept = np.polyfit(plot['Length'], plot['Max Accumulation'], 1)

plt.figure()
plt.scatter(plot['Length'], plot['Max Accumulation'])

plt.plot(plot['Length'], slope * plot['Length'] + intercept, color='black', label='Trendline')
for col_name, x, y in zip(plot.index, plot['Length'], plot['Max Accumulation']):
    plt.annotate(col_name, (x, y), textcoords="offset points", xytext=(0, 5), ha='center')

plt.xlabel('length of snow season (days)')
plt.xlim(0, 365)
plt.ylabel('max accumulation (in.)')
plt.ylim(0, 100)
plt.title('Length of Snow Season vs. Max Snow Accumulation (in snow water equivalent)')
plt.show()