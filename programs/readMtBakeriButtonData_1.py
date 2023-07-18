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
from sklearn.linear_model import LinearRegression


def regressionDatetime(df,colStr):
    # function returns the slope and intercept with 
    # appropriate dt for denominator of slope
    
    # df has index in datetime
    # colStr is the string that represents the column in df to be plotted
    
    df['datetime'] = df.index
    df['deltaT'] = df.datetime.diff().fillna(method = 'bfill')
    df['deltaThours'] = df.deltaT/pd.Timedelta(hours=1)
    
    x = df.datetime.apply(pd.Timestamp.toordinal);
    x = x.values.reshape(len(x), 1)
    y = df[strCol].values.reshape(len(x), 1);               # this is a strange step where
                                                            # an extra column needs to be added
    
                                                            # find the median dt to apply to slope
        
    modelT = LinearRegression();
    resultsT = modelT.fit(x,y);
    yModel = resultsT.predict(x);
    slope = resultsT.coef_
    slopeScaled = slope/df.deltaThours.min()
    intercept = resultsT.intercept_
    r2 = resultsT.score(x,df[strCol])

    plt.figure()
    plt.plot(df.datetime,x*slope+intercept,color = 'black')
    plt.plot(df.datetime,df.Value)
    
    



    

# location of data
fileLoc = '/home/michaeltown/work/esr/LSRI/2023/repos/MtBakerClimate/data/2018-2019/'
fileNames = os.listdir(fileLoc)
fileNames.sort()
fileNames = [f for f in fileNames if 'md' not in f]
# colNames = [c[:-4] for f in fileNames]
os.chdir(fileLoc)

# read the file
df = pd.read_csv(fileNames[0],header= 13)

# create datetime variable, set as index
df['datetime'] = pd.to_datetime(df['Date/Time'])
df = df.set_index('datetime')

# drop useless columns
df = df.drop(['Unit','Date/Time'],axis = 'columns')

# plot the temperature  time series
plt.figure()
plt.plot(df.index,df.Value)
plt.xlabel('Time')
plt.ylabel('Temperature (oC)')



# df = pd.DataFrame(columns = c)
# # read in files
# for f in fileNames:
#     df[f[:-4]] = pd.read_csv(f,header = 14)

