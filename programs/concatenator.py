"""
PROGRAM TO CONCATENATE PICKLED IBUTTON DATA FILES
_________________________________________________________________________

At the time of writing this code, I wanted to concatenate the data files
by Mt. Baker sites, such as 'site 1 buried' (folder: 1_buried) or
'site 5 west buried' (folder: 5west_buried)

So this code is adapted to this particular format:
C:/.../[my repository]/data/[folders by Mt.Baker site name]/[.pkl files]

All the basic code for concatenating files is in here. 
Some modifications might need to be made to adapt to different file path.
_________________________________________________________________________

@author: Zara Z. '24
"""

import pickle
import pandas as pd
import os

# Directory information
DATA_PATH = ""  # File path to iButton data folder

def concatenate(site_directory):
    pkl_files = [file for file in os.listdir(site_directory) if file.endswith(".pkl")]

    # Loop through site folder, concatenate all files
    data = []
    for file in pkl_files:
        file_path = os.path.join(site_directory, file)
        with open(file_path, 'rb') as f:
            df = pickle.load(f)  # Loads the pickle file as a dataframe
            data.append(df)

    concatenated_data = pd.concat(data)
    concatenated_data.sort_index(inplace=True)  # Sort by datetime index
    return concatenated_data

def main():
    # Site name (e.g. '1_buried', '5west_buried')
    site = input("Site: ")
    site_directory = os.path.join(DATA_PATH, site)

    # Load and concatenate data
    concatenated_data = concatenate(site_directory)

    # Save as a new pickle file
    os.chdir("")  # Enter the file path you wish to save to
    concatenated_data_name = site + '.pkl'  # File name format 1_buried.pkl, 5west_buried.pkl
    concatenated_data.to_pickle(concatenated_data_name)

if __name__ == "__main__":
    main()