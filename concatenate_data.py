import pandas as pd

df = pd.read_csv('iButtons_series.csv') # read iButton spreadsheet
listSites = df['Site'].unique() # get list of sites from spreadsheet

print("SITES")
for i in listSites:
    print(i)

site = input("Select a site: ")

if site in listSites:
    siteRows = df[df['Site'] == site]
    listTypes = siteRows.loc[siteRows['Type'].notnull(), 'Type'].unique()
    print("\nTYPES")

    for j in listTypes:
        print(j)

    type = input("Select a type: ")

    if type in listTypes:
        print("yay")
    else:
        print("Invalid type.")
else:
    print("Invalid site name.")