import matplotlib.pyplot as pt
import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

descLoc = {
    
    "Exposed": 0,
    "Buried": 1,
    "Shaded": 2
    
}

iButtons = pd.read_csv("data//iButtons.csv")

def getIndexFromDesc(site, desc):
    
    return (site - 1) * 3 + descLoc[desc]

def getiButtonNum(site, desc, year = "All"): #All: for debug purposes
    
    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    
    if year == "All":
        return iButtons.iloc[getIndexFromDesc(site, desc)][2:]
    
  
    num = iButtons.at[getIndexFromDesc(site, desc), year + " #"] if not pd.isna(iButtons.at[getIndexFromDesc(site, desc), year + " #"]) else -1
    if (num == -1):
        raise Exception("No iButton for specified description.")
  
    return iButtons.at[getIndexFromDesc(site, desc), year + " #"]
    
def getiButtonData(site: str, desc: str, year: str):
    
    if desc not in ["Buried", "Shaded", "Exposed"] or year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    return pd.read_csv("data//" + year + "//" + "MBCP" + year + "-" + str(int(year) + 1) + "_iButton" + getiButtonNum(site, desc, str(year)) + ".csv", skiprows=14, encoding="latin1")
    

def getAltitude(iButtonNum, year: str):
    
    if year not in ["2018", "2019", "2020", "2021", "2022"]:
        raise Exception()
    
    df = pd.read_csv("data//altitudes//altitudes" + year + ".csv", encoding="latin1")
    
    if not np.isnan(df.at[iButtonNum - 1, "Altitude (meters)"]):
        return df.at[iButtonNum - 1, "Altitude (meters)"]
    
    raise Exception("No altitude data.")

def toDecimalDate(date: str):
    
    x = date.split(" ")[0].split("/")
    
    return int(x[0])/12 + int(x[1])/365 + int(x[2])
                              
def getDataYears(site, desc, yrRange: str, ignoreMissingData: bool) -> list:
    
    years = yrRange.split("-")
    data = []
    times = []
    
    num = years[0]

    while (int(num) < int(years[1])):

        try:
            data += getiButtonData(site, desc, num)["Value"].tolist()
            times += getiButtonData(site, desc, num)["Date/Time"].tolist()
        except:
            
            if not ignoreMissingData:
                raise Exception("Missing data. Or check inputs.")
                
        
        num = int(num) + 1
        num = str(num)
    
    return data, times


#inputs: site, description (Buried, Exposed, Shaded), year range, false to throw an exception when
#missing data, true to just ignore it
data, times = getDataYears(1, "Buried", "2018-2021", False)

times = [round(toDecimalDate(x), 2) for x in times]

#you can also do pt.plot(times, data) and mess around with that
pt.scatter(times, data)

pt.xlabel("Decimal Date")
pt.ylabel("Celcius")

pt.show()




    
    











