# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:38:59 2023

@author: Zara
"""

# import
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os as os
import pickle
from sklearn.metrics import r2_score

directory = "H:/My Drive/School/LSRI/2023_ZaraZ/data/SNOTEL/Marten_Ridge_snowwater.csv"
myData = 'H:/My Drive/School/LSRI/2023_ZaraZ/data/pkl/1_buried'
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

sites = [file for file in os.listdir(myData) if file.endswith(".pkl")]

x_values = []
y_values = []

for site in sites:
    file_path = os.path.join(myData, site)
    with open(file_path, 'rb') as f:
        df = pickle.load(f)
        print(site)
        daily_mean_temp = df.resample('D').mean()
        daily_std_temp = df.resample('D').std()
        
        # Step 2: Create a boolean mask for snowdays based on the conditions
        snowday_mask = (
            (daily_mean_temp['Value'] >= -1) & 
            (daily_mean_temp['Value'] <= 1) & 
            (daily_std_temp['Value'] < 0.45)
        )
        
        # Step 3: Use the boolean mask to count the number of snowdays
        num_snowdays = snowday_mask.sum()
        x = num_snowdays
        y = slope * num_snowdays + intercept

        # Append x and y coordinates to the lists
        x_values.append(x)
        y_values.append(y)

        # Plot the scatter points for each site
        plt.scatter(x, y, label=site[4:13])  # 'label' argument sets the label for the legend
        plt.plot([x, 0], [y, y], linestyle='dashed', color='gray')

        # Step 4: Print or use the result as needed
        print("Number of snowdays:", num_snowdays)
        print()

plt.xlabel('# of snow days')
plt.xlim(0, 365)
plt.ylabel('peak snow water equivalent (in.)')
plt.ylim(0, 100)
plt.title('# of Snow Days vs. Peak Snow Water Equivalent')
plt.legend()
for x, y, site in zip(x_values, y_values, sites):
    plt.annotate(f' y={y:.2f}', (x, y), xytext=(5, 0), textcoords='offset points', color='gray', fontsize=9)
plt.show()