# Daily Logbook for Zara Z

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
