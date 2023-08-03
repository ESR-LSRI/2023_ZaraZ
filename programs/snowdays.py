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

# Calculate snowdays and snowamount for each column
snowdays = (df != 0).sum()  # Count non-zero values for each column
maxAccumulation = df.max()
print(maxAccumulation)

# Create a DataFrame with snowdays and snowamount as columns
snow_data = pd.DataFrame({'snowdays': snowdays, 'max accumulation': maxAccumulation})
slope, intercept = np.polyfit(snow_data['snowdays'], snow_data['max accumulation'], 1)

predicted_values = slope * snow_data['snowdays'] + intercept
total_sum_of_squares = ((snow_data['max accumulation'] - snow_data['max accumulation'].mean()) ** 2).sum()
residual_sum_of_squares = ((snow_data['max accumulation'] - predicted_values) ** 2).sum()

# Calculate R-squared value
r_squared = 1 - (residual_sum_of_squares / total_sum_of_squares)

plt.figure()
# Plot snowdays on the x-axis and snowamount on the y-axis
plt.scatter(snow_data['snowdays'], snow_data['max accumulation'])
plt.plot(snow_data['snowdays'], slope * snow_data['snowdays'] + intercept, color='black', label='Trendline')
for col_name, x, y in zip(snow_data.index, snow_data['snowdays'], snow_data['max accumulation']):
    plt.annotate(col_name, (x, y), textcoords="offset points", xytext=(0,5), ha='center')

plt.text(50, 80, f'R-squared = {r_squared:.2f}', fontsize=12)

plt.xlabel('# of snow days')
plt.xlim(0, 365)
plt.ylabel('max accumulation (in.)')
plt.ylim(0, 100)
plt.title('# of Snow Days vs. Max Snow Accumulation (in snow water equivalent)')
plt.show()