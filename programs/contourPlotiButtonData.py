# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 12:56:59 2017

@author: Mike.Town
"""

## program to make a contour plot of snow and near-surface air temperature data.

import importlib
import os as os             # for moving around the operating system
import scipy as scipy
import matplotlib.pyplot as plt
import numpy as np
import pickle, shelve
from scipy.interpolate import UnivariateSpline


dataFileLocation = input('Enter the case-sensitive location of the iButton data file: ');
os.chdir(dataFileLocation);
dirContents = os.listdir('.');

## filter out the csv, txt, and xlsx files to leave only the dat files in the directory
step = 0;
length = len(dirContents)
while step < length:
    if dirContents[step].endswith('.dat'):
        step = step + 1;
    else:
        dirContents.remove(dirContents[step]);
        step = 0;
        length = len(dirContents);


dirContents.sort();

print('A list of the *.dat files to choose from.');
i = 0;
while i < len(dirContents):
    print(str(i) + '\t' + dirContents[i]);
    i = i + 1;

## get the number of data files to plot
numDataFiles = int(input('How many files are there to plot? '));


# loop to build contour plot list
depth = [];

print('We are going to make a contour plot of the data.\n You will select the necessary binary (*.dat) files and enter the corresponding depth of each of the data files.');

i = 0;
while i < numDataFiles:
    dataFileNum = int(input('Enter the number of data file number ' + str(i+1) + ': '));
    depthTemp = input('Enter the depth associated with this data file (m): ' );
    depth.append(float(depthTemp));
    fileBinary = open(dirContents[dataFileNum],'rb');

    dateTime = pickle.load(fileBinary);
    year = pickle.load(fileBinary);
    month = pickle.load(fileBinary);
    day = pickle.load(fileBinary);
    hour = pickle.load(fileBinary);
    minute = pickle.load(fileBinary);
    second = pickle.load(fileBinary);
    td = pickle.load(fileBinary);
    T = pickle.load(fileBinary);
    unit = pickle.load(fileBinary);
    fileBinary.close();

    ## create the host matrix and load the first vector of the temperature depth array
    if i == 0:
        T_depth = np.zeros((numDataFiles,len(T)));        
        T_depth[i,:] = np.asarray(T);

        timeVec = np.zeros((1,len(T)));
        timeVec = np.asarray(td);
    # interpolate the current data set to the initial time series time vector
    else:
        T_spline = UnivariateSpline(td,np.asarray(T),k=3);
        T_depth[i,:] = T_spline(timeVec);
    
    i = i + 1;


## plot the individual time series on the same plot to check the data loading script        
fig1 = plt.figure();
plt.hold;
i = 0;

while i < numDataFiles:
    plt.plot(timeVec,T_depth[i,:]);
    i = i + 1;

plt.show();


## now make the color contour plot
start = -8;
stop = 8;
steps = np.linspace(start,stop,(stop-start)*4+1); # contouring intervals in degrees C with 0.25 oC resolution
fig2 = plt.figure();
plt.contourf(timeVec,depth,T_depth,steps);
plt.set_cmap('bwr');    ## a prescribed colormap (could be 'gray')
plt.colorbar(orientation= 'horizontal');
plt.xlabel('time (decimal day)');
plt.ylabel('height above surface (m)');
plt.title('Temperatures ($\degree$C) for Copper Creek 20190207');
#plt.title('Temperatures ($\degree$C) for ' + dirContents[dataFileNum][-12:-4]);
plt.xlim([0, 365])
plt.show();

#os.chdir('./figures');
fig2.savefig('snowTempContourCopperCreek20190207'+'pdf');
fig2.savefig('snowTempContourCopperCreek20190207' +'jpg');


## questions: how do you change the colormap? how do you efficiently create an array in np?