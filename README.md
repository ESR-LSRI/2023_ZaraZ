# Zara Z '24 - repository for research into snow cover duration and snow accumulation

### Introduction
My time at LSRI 2023 was devoted to examining:
1) snow cover duration of Mt. Baker at different elevations; and
2) the relationship between snow cover duration and snow accumulation at Schrieber's Meadow in particular

Snow is not only directly _impacted_ by rising temperatures, but also _impacts_ the amount of water we get from snowmelt. Therefore, understanding snow patterns on Mt. Baker is helpful for comprehending the broader implications of climate change in the PNW and for mitigating its impact on vulnerable communities.

### Table of Contents
The structure of my repository is as follows:
* MtBakerData: original iButton data in csv format, organized in folders by year
* data
  * SNOTEL
    * SnowDepth
      * .csv files: SNOTEL data for Marten Ridge, separated by year, csv format
      * MartenRidge_SnowDepth_2018-2023.pkl: curated SNOTEL data containing only snow depth, concatenated across 2018-2023, pickled.
    * Marten_Ridge_snowwater.csv: SNOTEL snow water equivalence (SWE) data for Marten Ridge
    * snowwater_cut.csv: Marten_Ridge_snowwater.csv with only columns for each year
  * SnowDensity
    * MartenRidge_SWE_2018-2023.pkl: curated SNOTEL data containing only SWE, concatenated across 2018-2023, pickled
    * MartenRidge_SnowDepth_2018-2023.pkl: curated SNOTEL data containing only snow depth, concatenated across 2018-2023, pickled (duplicate from ./data/SNOTEL/SnowDepth)
  * original: original iButton data in csv format, organized by site and installation method
  * pkl: curated iButton data containing only datetime data and temperature readings, organized by site and installation method, pickled
  * snow_cover: curated iButton data for buried iButtons only, concatenated by site
* docs
  * poster_ASnowyStory.pdf: poster presenting my research on snow duration
* figures: a large variety of different visualizations from iButton and SNOTEL data
* programs: a large [variety] of python programs for data analysis and visualization

[variety]: # (can you make a list of important code here?)

* dailyLogbook.md: logbook detailing my daily work during LSRI

### Additional Info
* All programs were written in Spyder (Anaconda)
