#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:46:47 2023

Read Mt. Baker Data

@author: michaeltown
"""

# libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os as os

# location of data
fileLoc = '/home/michaeltown/work/esr/LSRI/2023/repos/MtBakerClimate/data/2018-2019/'
fileNames = os.listdir(fileLoc)
# colNames = [c[:-4] for f in fileNames]
os.chdir(fileLoc)

# read the file
df = pd.read_csv(fileNames[0],header= 13)

# create datetime variable, set as index
df['datetime'] = pd.to_datetime(df['Date/Time'])
df = df.set_index('datetime')

# drop useless columns
df.drop(['Unit','Date/Time'],axis = 'columns',inplace = True)

# plot the temperature  time series
plt.figure()
plt.plot(df.index,df.Value)
plt.xlabel('Time')
plt.ylabel('Temperature (oC)')



# df = pd.DataFrame(columns = c)
# # read in files
# for f in fileNames:
#     df[f[:-4]] = pd.read_csv(f,header = 14)

