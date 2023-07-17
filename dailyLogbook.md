
# Daily Logbook for Zara

___________________________________________________________________________________________________________

## 17 July: Concatenating data (continued), plotting

### Problem with 2019 sensors 9 and 10 (site 5 west slope vs ridge)
2019 sensors 9 and 10 were given the same lat/long in the logbook with no additional site description, making it difficult to find which one was at west slope and which one at top ridge. The only way to distinguish them would be by looking at the data itself.

I decided to **graph the west slope and top ridge sensors from 2018** to find any patterns that might be comparable to 2019 sensors 9 and 10. Here's what I got:
* West Slope: ![image](https://github.com/ESR-LSRI/2023_ZaraZ/blob/main/figures/2018_5west_buried.png)
* Top Ridge: ![image](https://github.com/ESR-LSRI/2023_ZaraZ/blob/main/figures/2018_5ridge_buried.png)

As Dr. Town predicted, **the snow cover at top ridge went away much earlier than that at west slope**. With this information, I can graph 2019 sensors 9 and 10 in the same way and **pretty safely assume that the one with earlier snowmelt was the one at top ridge**.
* 2019 sensor 9: ![image](https://github.com/ESR-LSRI/2023_ZaraZ/blob/main/figures/2019_mystery_9.png)
* 2019 sensor 10: ![image](https://github.com/ESR-LSRI/2023_ZaraZ/blob/main/figures/2019_mystery_10.png)

Since snow cover as indirectly measured by 2019 sensor 10 went away much earlier than that by sensor 9, I'm going to conclude that **sensor 9 was at west slope and sensor 10 was at top ridge**.

Now we are able to concatenate their data to the right dataframes.

### Plotting
* code now works to plot a time vs temperature graph
  * reads csv into dataframe
  * drops irrelevant columns
  * re-formats 'Date/Time' string into data of type datetime
  * sets datetime as index
  * plots graph with index for x and Value (temperature) for y
![image](https://github.com/ESR-LSRI/2023_ZaraZ/blob/main/figures/2018_1_buried.png)

### Concatenating data
* ~working to create folders for each site so code can simply loop through the folder~ **done, and pushed to teammates' directories :)**
* **next step: concatenate data for site 1 buried**

### 2023 data
* java and OneWire are set up, 2023 data are ready to be read into csv files

___________________________________________________________________________________________________________

## 14 July: Concatenating data, identifying relevant sensors for snow extent

### Problems
* **2020 sensors 2 and 4 were snag sensors placed at different heights than any other year ([163 and 190] cm respectively, compared to 50-100-150-200-230). Is this trivial enough that we can round them to 150 and 200?**
* **2019 sensors 9 and 10 were given the same coords with no additional site description, making them indistinguishable between site 5 west slope vs top ridge. Sensor 11 is assumed to be east slope only because its coords were NE of the coord given for 9 and 10**
  * the only way to tell might be through the data --> **if there was a layer of snow covering both sensors at some point, the one at top ridge likely melted/went away faster due to windier conditions**

Helpful website for finding altitude from lat/long: [caltopo.com](caltopo.com) map
* elevation we got from Google Maps is being checked for a 2nd time by Kaiden using caltopo for the sake of consistency and accuracy.

### Look at data for Mt. Baker temperature
* for day hike!

### modifying table to include more specific data
* Concatenating the data across the years is helpful so that we can refer to just one file for all the data at a single location/depth/height. Can be thought of as data that we would have gotten if we had one 5-year sensor in that location
* our tables do not currently specify the height and depth at which the sensors were buried
  * need to make this distinction at least for **tree(exposed)** category --> the series of sensors at different heights of the snag
    * the depth for the buried category does not need to be specified for now. they are all around the same anyway and it's just one of many other variables that are hard to keep consistent
* table should have a new column that specifies the height and depth
  * this way we do not need to hard code the list of corresponding censors, instead we can just read in from the spreadsheet
* site 5 specifically should be separated into **west slope, east slope, and top ridge**

### site 5, microclimates, and additional information
* table categorizes all three site 5 sensors as **buried** and did not make the distinction between their slightly different microclimates
* site 5 sensors were placed at west ridge (grassy), ridge top (windy), and east ridge (glacial/mars)
  * data from these three sensors can be compared to study microclimates
* **for research into snow extent, the sensor at buried at west ridge would probably be the best "macro-scale" representation of site 5 according to Dr. Town**
  * all other sites of the sensors were selected to be a macro-scale representation of their respective biomes too, so the data can pick up on the differences across them
* **next step: account for microclimates in the table**

### future research questions
* what different types of microclimates are on Mt. Baker?
* **how does snow interact differently with each microclimate?** (really interesting)
  * the darker the surface the faster the snow melts (reflectivity)
  * when there's a deep layer of snow it doesn't really matter, but when it begins to thin out, the rate at which the snow melts on surfaces varies greatly
    * ex. snow melts faster on pavement than it does on grass

### [Group tasks]
* concatenate data across the years, in an intuitive order (by site? by individual research questions?)
  * each group member concatenates a different set of data so we have more progress
    * I believe Noah is currently working on 2021-22 sensors #3-7 (the snag)
    * **next step (for me): concatenate data for the buried sensors by elevation (from low to high)**
 

 [163 and 190]: # (let's keep it as accurate as we can. The lapse rate can be sensitive near the surface.)
[Group tasks]: # (Great logbook entries)
___________________________________________________________________________________________________________

## 13 July: Data munging and logbooks (continued)

Group is working together to organize our data into better formats (plotting a map, transcribing to Google Sheets)

### Group to-do list
* ~Finish logbook v2~
  * ~separate pages for each year~
* verify iButton table 
* ~lat/long conversion (if time, today)~
  * **next step: location consistency between coords**
* plotted maps for each year
* updating notes + assumptions file
  * turn into markdown file
* import function for iButtons
  * convert time values to "datetime"
* finding altitude from lat/long

### Lat/long consistency
* latitude/longitude conversion: there is bound to be some discrepancy when converting between the different formats
* **Q: what is the threshold we set for identifying whether two lat/long measurements are actually refering to the same location?**
  * might just have to use best judgement and check logbook for site number
  * can average the lat/long coords
* we have converted all coords to **degree-minute-second format**
  * **next step: location consistency (see question)**

### Finding altitude from lat/long
* We're doing this manually via Google Maps --> not efficient and prone to human error
* **some altitudes we found via Google Maps are inconsistent with what was recorded in the logbooks**
  * inconsistencies highlighted in red in the spreadsheet

### Things to investigate
* when the 2021 group collected the 2020 sensors, they reported finding sensor 1 in 3's spot and 3 in 1's spot
  * **next steps: we can identify what happened when analyzing the data later, because one was supposed to be buried and the other on a tree and [shaded]**

[shaded]: # (let's start concatenating and plotting the data at each level. Create a pkl and csv file for each level. Focus on the levels that you will use for your question. )
___________________________________________________________________________________________________________

## 12 July: Data munging and logbooks

The iButton sensors were not installed in consistent locations from year to year between 2018-2022 --- for example, in some years sensor 3 replaced sensor 1, and we can only tell by checking the logbook.

### Google Sheets matching locations and sensors between the years ([spreadsheet](https://docs.google.com/spreadsheets/d/1rYSfCRtbOYoHYn_85mbR3-nh_1uO19BrHjO-JNV4u0A/edit?usp=sharing))
* columns and rows are organized by year and location respectively
* number in individual cells represent the iButton # at the corresponding year and location
* this can help us easily track iButton switches/changes at any particular location

### Plotting sensor location using My Map
* each sensor location was marked with a pin at the long/lat indicated by the logbooks
* pins were categorized into tree (shaded), tree (exposed), and buried
  * My Map allows the user to select and unselect the categories, which could be very helpful if we ever want to identify just one type of sensor.
* five maps total, one for each year
* makes it easier to visually understand where the sensors are
* **next steps: finish the maps**

### Keeping track of notes and assumptions ([doc](https://docs.google.com/document/d/1t3DZDcdIQ3F8V3vs7w8JFYGRBkURkfGAyaJHBlQ6oHY/edit?usp=sharing))
* some logbooks had many pieces of missing information, such as location and installation data
* I am able to fill in most of the missing information by refering to any notes made and/or the logbooks of the consecutive years, but **all such assumptions need to be recorded in case we later run into inconsistent data**

### Logbooks "Version 2"
* original logbooks messy and hard to keep track of
* we are transcribing and organizing all the information into Google Sheets to make it easier to plot the map
  * iButtons are organized by #
  * any missing location/installation data are filled in to the best of our ability (and any assumptions/additional notes recorded)
* **next steps: finish Logbooks Version 2**
* **collection notes are made by the group of the *following year*, upon retrieving the sensors installed in the *current year* of the logbook!!!**
  * **next steps: go back and re-evaluate location/installation assumptions**
  * finished up till 2020
* **there is some confusion for 2020 iButtons 1 & 3; 2021 group reported finding 3 in 1's spot and 1 in 3's spot**

Additional notes:
* would be great to have one place for all of our files
* **Q: where to draw the line for reasonable vs unreasonable assumptions?**
___________________________________________________________________________________________________________

## 11 July: Understanding [paper about snow cover](https://github.com/ESR-LSRI/MtBakerClimate/blob/main/docs/references/Lundquist_Lott_Tsnow_2008WR007035.pdf), introduction to research questions

### Understanding "Using inexpensive temperature sensors to monitor the duration and heterogeneity of snow-covered areas"
Near-surface soil usually experience diurnal (read: daytime) temperature changes, but not when it is covered by a layer of snow (serves as insulator, and sends infrared light back to space). Thus, sensors placed in near-surface soil can indirectly measure snow cover using temperature data by analyzing the time elapsed between periods of diurnal temperature changes combined with air temperature record and snow melt data.

### RQ 1: What is the lapse rate (how temperature changes with height) on Mt. Baker? How does this change with season? (Felicity indicated interest)
* 5 years of data from iButtons to work with
* Many factors affect lapse rate, such as moisture and cloud cover
* the lapse rate we calculate would be empirical and can be compared with the theoretical lapse rate derived by ERA5 (some kind of model)
* Q: if our results are inconsistent with that of ERA5, which do we trust?

### RQ 2: What is the seasonal snow extent on Mt. Baker? Has this changed over the instrument record? (my interest here)
* snow cover paper relevant
* data lacking for the south side of Mt Baker
* can indirectly measure snow cover via near-surface soil temperatures --- 0 degrees Celsius or below indicate that there is snow cover (when ground warming the snow and melted snow cooling the ground reach an equilibrium?)
* the snow cover days we observe can be compared with data from ERA5
* **next steps: visualization of snow cover duration vs elevation over the course of 5 years**
  * [Tanvi's data visualization showing snow cover duration by elevation for 1 year](https://resources.finalsite.net/images/f_auto,q_auto/v1595276787/lakeside/pcvib3itvln0ceohblhw/FIg2_tanvi.png)
  * scatter plot, each color representing one winter --> see if there's any trend
  * Q: Over the course of 5 years, has there been a change in snow cover duration on the south side of Mt Baker? (3 graphs? 1 graph?)
    * date of snowfall onset? **next steps: define onset (search up standard/commonly-accepted definition)**
    * date of snowmelt? **same as above**
* **Q: How do I figure out which sensors are relevant for this question as well as their elevation?** 
  * **next steps: check logbooks**
    * buried vs tree (only buried is relevant for this right?)
  * is there a map that shows the location/elevation of the sensors visually?

### RQ 3: How sunny is it at Schrieber's Meadow (the lowest instrument site)? Has this changed over the instrument record? (Noah or Kaiden)
### RQ 4: What is the seasonal snow depth at Schrieber's Meadow in 2021-2022? (Noah or Kaiden)

___________________________________________________________________________________________________________

## 10 July: Learning how to read papers, and the stuff I learned from one [particular paper](https://github.com/ESR-LSRI/MtBakerClimate/blob/main/docs/references/Lundquist_Huggett_Tintrees_2008WR006979.pdf)

Going into this I didn't have much background knowledge on meterology/glaciology/oceanography, so I found some of the papers a difficult read due to the terminology used and the fancy language :D. It looks more complicated than it actually is, so I know that as long as I can put what I learned into my own words it makes more sense.

### Understanding "[Evergreen trees as inexpensive radiation shields for temperature sensors](https://github.com/ESR-LSRI/MtBakerClimate/blob/main/docs/references/Lundquist_Huggett_Tintrees_2008WR006979.pdf)"
I was initially confused on how this paper helps me with understanding how to use data from the sensors, because I expected more like an instruction sheet. After conferring with Dr. Town, I understood that the paper is actually addressing how putting the sensors under Evergreen trees helps us monitor the temperature without the influence of the sun's radiation, and that Evergreen trees serve as a good enough radiation shield. 

This is important as monitoring the temperature changes of Mt. Baker is a significant part of our research question, so ensuring that the data we gather from the sensors are accurate is of the utmost importance.

Next steps: read the abstracts of the two other papers provided and understand their significance to our research. I am especially interested in the snow one.

[particular paper]: # (great work identifying your gaps in knowledge and what you need to do to fill them.)

___________________________________________________________________________________________________________

## Date: Topic(s) of the day

Your daily log book should include the following contents:
* Questions you were asking/tasks you needed to complete
* Details on your approach to those questions/task
* A summary of outcomes (e.g. answers, numbers, graphs, intermediate products)
* Your next steps
* Questions you have for your peer(s) and/or instructor(s) 

*each of the topics below should contain a complete summary as detailed above*

This is a [link](https://www.markdownguide.org/basic-syntax) markdown syntax. Thanks for learning this!

### Topic/question/task 1
Summary of question/task
details of approach
summary of outcomes
next steps
questions
