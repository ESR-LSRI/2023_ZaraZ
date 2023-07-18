# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:35:43 2017

@author: Mike.Town
"""

## Program to import iButton temperatures from the native file, turn the time data into a Julian Date and save it as .txt file.

## go to the data direction

import os as os             # for moving around the operating system
import matplotlib.pyplot as plt
import numpy as np
import pickle
from scipy.interpolate import UnivariateSpline

## find location of the iButton temperature data file
dataFileLocation = input('Enter the case-sensitive location of the iButton data file: ');
os.chdir(dataFileLocation);
dirContents = os.listdir('.')
dirContents.sort();

i = 0;
while i < len(dirContents):
    print(str(i) + '\t' + dirContents[i]);
    i = i + 1;
    
## retrieves the correct file from the user
dataFileNum = int(input('Enter the number of the data file: '));
dataFile = open(dirContents[dataFileNum],'r');
data = dataFile.readlines();
dataFile.close();

## remove excess lines of header data
data = data[15:len(data)];

## while loop to split data up into data/time info, units, and temperature measurement lists

dateTime = [];
unit = [];
T = [];


unit = [];          # temperature unit (Celsius)
T = [];             # temperature
year = [];
month = [];
day = [];           # day of the month      
hour = [];
minute = [];
second = [];
td = [];            # convert the day into a decimal day value


## use this for converting hours minutes seconds to days https://matplotlib.org/api/dates_api.html

i = 0;

while i < len(data):
    
    ## splits the data into appropriate variables
    dateTimeTemp, unitTemp, T_Temp = data[i].split(','); 
    monthDayYear, time_Temp = dateTimeTemp.split(' ');
    month_Temp, day_Temp,year_Temp = monthDayYear.split('/');
    hour_Temp, minute_Temp = time_Temp.split(':');

    ## clean up the strings to be processed by np.datetime64 - a better solution has got to exist in python...
    if int(month_Temp) < 10:
        month_Temp = '0' + month_Temp;
    if int(day_Temp) < 10:
        day_Temp = '0' + day_Temp;
    if (int(hour_Temp) < 10):  # & (int(hour_Temp) != 0):
        hour_Temp = '0' + hour_Temp;
        
    ## appends separated data points into categorized lists
    dateTime.append(dateTimeTemp);
    year.append(int(year_Temp));
    month.append(int(month_Temp));
    day.append(int(day_Temp));
    hour.append(int(hour_Temp));
    minute.append(int(minute_Temp));

    ## time difference from the beginning of the year.
    td_Temp = np.datetime64(year_Temp + '-' + month_Temp + '-' + day_Temp + 'T' + hour_Temp + ':' + minute_Temp) - np.datetime64(year_Temp + '-01-01T00:00');
    td_Temp = td_Temp / np.timedelta64(1,'s'); ## converts this into a decimal seconds value
    td_Temp = td_Temp/86400; # converts this into a decimal day value.

    ## appends the day of the year to a list
    td.append(td_Temp);
    unit.append(unitTemp);
    T.append(float(T_Temp));

    i = i + 1;
  

  
T_spline = UnivariateSpline(td,np.asarray(T),k=3);


## next steps are write the text data file, python data file, figure out the day of year list

## write the data into a more forgiving text file

dataFile = open(dirContents[dataFileNum][:-3]+'txt','w');
dataFile.write('Date/time, year, month, day, hour, minute, seconds, decimal day, Temp, units\n');
dataFile.write('\n');

i = 0;
 
while i<len(td):
    dataFile.write(str(dateTime[i]) + ', ' + str(year[i]) + ', ' + str(month[i]) + ', ' + str(day[i]) + ', ' + str(hour[i]) + ', ' + str(minute[i]) + ', ' + str(td[i]) + ', ' + str(T[i]) + ', ' + unit[i] + '\n');
    i = i + 1;

dataFile.close();
    
## pickle the data into a binary data file
fileBinary = open(dirContents[dataFileNum][:-3] + 'dat','wb+');
pickle.dump(dateTime,fileBinary);
pickle.dump(year,fileBinary);
pickle.dump(month,fileBinary);
pickle.dump(day,fileBinary);
pickle.dump(hour,fileBinary);
pickle.dump(minute,fileBinary);
pickle.dump(second,fileBinary);
pickle.dump(td,fileBinary);
pickle.dump(T,fileBinary);
pickle.dump(unit,fileBinary);
fileBinary.close();

## reminder - load these data in the same order in which they were 'dumped'


## check the data by plotting and showing the figure to the user
## histogram of iButton temperature data
plt.figure(1)
bins = np.arange(0, 25, 0.5)
plt.hist(T, bins, color = 'blue');
plt.ylabel('Number of Days');
plt.xlabel('T (oC)');
plt.title('Temperature Histogram');
plt.show();

## user input of what year the data starts
year0 = int(input('What is the first year of the data? '))

## appending days that spans two years into different lists
year1 = [];
year2 = [];
i = 0
while i < len(year):
    if year[i] == year0: 
        year1.append(td[i]) # days in the first year
    else:
        year2.append(td[i]) # days in the second year
    i = i + 1

## appending temperatured data spanning two years into lists that correspond with the year lists
T1 = [];
T2 = [];
i = 0
while i < len(year):
    if i < len(year1):
        T1.append(T[i])
    else:
        T2.append(T[i])
    i = i + 1

## time series of temperature data vs. time
plt.figure(2)
plt.plot(year1,T1,'ro-',label='Temperature in ' + str(year0)); # only plots temperature data over 2 years, can be more adaptable
plt.plot(year2,T2,'bo-',label='Temperature in ' + str(year0 + 1));
plt.ylabel('T (oC)');
plt.xlabel('Day of year');
plt.title('Temperature vs. Time for ' + dirContents[dataFileNum][0:8] + ' for ' + dirContents[dataFileNum][8:18]);
plt.grid(True);
plt.legend(loc='upper right');
plt.xlim([0, 365]); # change according to how many days of the year need to be shown
plt.show();

## save data to the figure folder
#os.chdir('../../figures');
#fig.savefig(dirContents[dataFileNum][:-4]+'.pdf');
#fig.savefig(dirContents[dataFileNum][:-4]+'.jpg');

## code to output exsitance of snow cover
## finds the daily mean temperature
i = 0
dmean = []
while i < len(T) - len(T)%6:
    dmean.append((T[i] + T[i + 1] + T[i + 2] + T[i + 3] + T[i + 4] + T[i + 5])/6)
    i = i + 6

## finds the daily temperature standard deviation based on the daily mean
snowsd = []
i = 0
while i < len(dmean):
    snowsd.append((((T[i*6] - dmean[i])**2 + (T[i*6 + 1] - dmean[i])**2 + (T[i*6 + 2] - dmean[i])**2 + (T[i*6 + 3] - dmean[i])**2 + (T[i*6 + 4] - dmean[i])**2 + (T[i*6 + 5] - dmean[i])**2)/6)**(1/2))
    i = i + 1

## calculates snow cover based on daily temperature standard deviation < 1.5
snow = []
i = 0
while i < len(T):
    if T[i] >= 2:
        snow.append(0)
    else:
        if snowsd[int(i/6)] < 1.5: # limit does not have to be 1.5 and can be made adaptable
            snow.append(1) # 1 = snow
        else:
            snow.append(0) # 0 = no snow
    i = i + 1

## calculates snow cover based on consistent temperatures for 3 data points
snow1 = []
i = 0
while i < len(T):
    if T[i] > 1.5:
        snow1.append(0)
    else:
        if T[i] == T[i + 1] and T[i + 2]: # does not have to be equal, could be 0.5 apart
            snow1.append(1)
        elif T[i] == T[i + 1] and T[i - 1]:
            snow1.append(1)
        elif T[i] == T[i - 1] and T[i -2]:
            snow1.append(1)
        else:
            snow1.append(0)
    i = i + 1
    
## calculates snow cover based on a daily mean temperature of less than 2 and a daily temperature standard deviation of less than 2
snow2 = []
td2 = []
i = 0
while i < len(dmean):
    if dmean[i] < 2 and snowsd[i] < 2:
        snow2.append(1)
    else:
        snow2.append(0)
    td2.append(td[i*6])
    i = i + 1

## time series of snow cover calculated with standard deviation  
plt.figure(3)
plt.plot(td,snow,'g-',label = 'Snow Cover at Lakeside School (Using Standard Deviation)')
plt.ylabel('snow(1) or no snow(0)');
plt.xlabel('Day of year');
plt.grid(True);
plt.legend(loc='upper right');
plt.xlim([0, 64]);
plt.ylim([0,1.5]);
plt.show();

## times series of snow cover calculated with temperature stability
plt.figure(4)
plt.plot(td,snow1,'g-',label = 'Snow Cover at Lakeside School')
plt.ylabel('snow(1) or no snow(0)');
plt.xlabel('Day of year');
plt.grid(True);
plt.legend(loc='upper right');
plt.xlim([0, 64]);
plt.ylim([0,1.5]);
plt.show();

## scatterplot of daily mean temperature and daily temperature standard deviation
plt.figure(5)
plt.scatter(dmean, snowsd)
plt.xlabel('Daily Mean Temperature');
plt.ylabel('Daily Temperature Standard Deviation');
plt.show();
C_MeanSD = np.corrcoef(dmean, snowsd) # calculates correlation coefficient of daily temperature mean and standard deviation

## time series of snow cover calculated with daily mean temperature and daily temperature standard deviation
plt.figure(6)
plt.plot(td2,snow2,'g-',label = 'Snow Cover at Lakeside School (Using Stand. Deviation and Mean Temp.)')
plt.ylabel('snow(1) or no snow(0)');
plt.xlabel('Day of year');
plt.grid(True);
plt.legend(loc='upper right')
plt.xlim([0, 64]);
plt.ylim([0,1.5]);
plt.show();

## histogram of days with snow cover calculated with standard deviation
plt.figure(7)
bins = np.arange(0, 3, 0.5)
plt.hist(snow, bins, color = 'blue');
plt.ylabel('Number of Days');
plt.xlabel('Snow(1) or No Snow(0)');
plt.title('Snow Histogram (Using Standard Deviation)');
plt.show();

## histogram of days with snow cover calculated with temperature stability
plt.figure(8)
bins = np.arange(0, 3, 0.5)
plt.hist(snow1, bins, color = 'purple');
plt.ylabel('Number of Days');
plt.xlabel('Snow(1) or No Snow(0)');
plt.title('Snow Histogram');
plt.show();


## iButton vs. met station data
## met station data might be off by a few days and records every 5 minutes
## find location of the met station data file
dataFileLocation = input('Enter the case-sensitive location of the Met Station data file. If you do not have this file, press Enter: ');
os.chdir(dataFileLocation);
dirContents = os.listdir('.')
dirContents.sort();

i = 0;
while i < len(dirContents):
    print(str(i) + '\t' + dirContents[i]);
    i = i + 1;
    
## retrieval of the correct data file from user
dataFileNum = int(input('Enter the number of the data file: '));
dataFile = open(dirContents[dataFileNum],'r');
data = dataFile.readlines();
dataFile.close();

## remove excess lines of header data
data = data[6:len(data)];

## while loop to split data up into data/time info, units, and temperature measurement lists

dateTime = [];
unit = [];
T = [];


unit = [];
T = [];
year = [];
month = [];
day = [];           # convert the day into a decimal day value
hour = [];
minute = [];
second = [];
td = [];
otemp = [];
ohum = [];


## use this for converting hours minutes seconds to days https://matplotlib.org/api/dates_api.html

i = 0;

while i < len(data):
    
    ## splits data into appropriate catergories
    DateTime, Year, Month, Day, Hour, Minute, Second, tD, OutTemp, OutHumidity = data[i].split(',');
    
    ## if there is no data for a certain time, it shows up as None, which has to be changed to NAN for Python to read it
    if OutTemp == ' None':
        OutTemp == 'NAN'
    elif OutHumidity == ' None':
        OutHumidity == 'NAN'
    else:
        dateTime.append(DateTime);
        year.append(int(Year));
        month.append(int(Month));
        day.append(int(Day));
        hour.append(int(Hour));
        minute.append(int(Minute));
        second.append(int(Second));
        td.append(float(tD));
        otemp.append(float(OutTemp));
        ohum.append(float(OutHumidity));
    
    i = i + 48 # iButton data records every 4 hours and met station records every 5 minutes


## pickle the data into a binary data file
fileBinary = open(dirContents[dataFileNum][:-3] + 'dat','wb+');
pickle.dump(dateTime,fileBinary);
pickle.dump(year,fileBinary);
pickle.dump(month,fileBinary);
pickle.dump(day,fileBinary);
pickle.dump(hour,fileBinary);
pickle.dump(minute,fileBinary);
pickle.dump(second,fileBinary);
pickle.dump(td,fileBinary);
pickle.dump(T,fileBinary);
pickle.dump(unit,fileBinary);
fileBinary.close();

## time series of outdoor temperature at Lakeside
plt.figure(9)
plt.plot(td,otemp,'b-',label = 'Outdoor Temperature at Lakeside School')
plt.ylabel('Outdoor Temperature');
plt.xlabel('Day of Year');
plt.grid(True);
plt.legend(loc='upper right');
plt.xlim([0, 100]); # the outdoor temperature data only goes for around 92 days
plt.ylim([-10,30]);
plt.show();

## time series of outdoor humidity at Lakeside
plt.figure(10)
plt.plot(td,ohum,'b-',label = 'Outdoor Humidity at Lakeside School')
plt.ylabel('Outdoor Humidity');
plt.xlabel('Day of Year');
plt.grid(True);
plt.legend(loc='lower right');
plt.xlim([0, 100]);
plt.ylim([0,100]);
plt.show();

## scatterplot of outdoor temperature and humidity
plt.figure(11)
plt.scatter(otemp, ohum)
plt.xlabel('Outdoor Temperature');
plt.ylabel('Outdoor Humidity');
plt.show();
C_TempHum = np.corrcoef(otemp, ohum) # calculates correlation coefficient of outdoor temperature and humidity

## scatterplot of outdoor and soil temperature
plt.figure(12)
otemp = otemp[:-(len(otemp)-len(T2))]
plt.scatter(otemp, T2)
plt.xlabel('Outdoor Temperature');
plt.ylabel('Soil Temperature');
plt.show();
C_OutSoilTemp = np.corrcoef(otemp, T2) # calculates correlation coefficient of outdoor and soil temperature

## time series of both iButton temperature data and met station temperature data
plt.figure(12)
td = td[:-(len(td)-len(T2))] # met station data is shorter, so iButton data has to be shortened to the same length here
plt.plot(td,otemp,'b-',label = 'Outdoor Temperature at Lakeside School')
plt.ylabel('Outdoor Temperature and Soil Temperature');
plt.xlabel('Day of Year');
plt.grid(True);
plt.legend(loc='upper right');
plt.xlim([0,70]); # the data points only overlap for around 60 days
plt.ylim([0,20]);
plt.plot(td,T2,'r-',label = 'Soil Temperature at Lakeside School')
plt.grid(True);
plt.legend(loc='upper right');
plt.show();
