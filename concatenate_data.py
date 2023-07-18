#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os as os

# IMPORTANT: FILES ARE STRUCTURED DIFFERENTLY

fileLoc = 'G:/My Drive/School/LSRI/2023_ZaraZ/data/1_buried'
fileNames = os.listdir(fileLoc)
# colNames = [c[:-4] for f in fileNames]
os.chdir(fileLoc)

file = fileNames[0]

df = pd.read_csv(file, encoding="unicode_escape", header=13)

# create datetime variable, set as index
df['datetime'] = pd.to_datetime(df['Date/Time'])
df = df.set_index('datetime')

# drop useless columns
df.drop(['Unit','Date/Time'],axis = 'columns',inplace = True)

# plot the temperature  time series
plt.figure()
plt.plot(df.index,df.Value)
plt.title(file)
plt.xlabel('Time')
plt.ylabel('Value')

#plt.figure()
#plt.plot(df)
