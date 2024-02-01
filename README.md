# Biodiversity - data analyse

## Introduction

This goal of this project is to analyze biodiversity data from the National Parks Service, particularly around various species observed in different  locations.
The data is not real and is provided by codecademy.com



## Scpping

To help quide a projekt proces there are four sections to follow:
- Project Goals
- Data
- Analysis
- Evaluation

1. In this project I analyse two csv files from National Parks Service. The main goal is understanding characteristics about species and their conservation status.
There are four main questions:

- What is the distribution of conservation status for species?
- Are certain types of species more likely to be endangered?
- Are the differences between species and their conservation status significant?
- Which animal is most prevalent and what is their distribution amongst parks?

2. There are two csv files. First csv file has information about species and another one has observations about species in the national parks.

3. We need to check:
   - distributions
   - relationship between species
   - species conservation status
   - observations of species in parks
  
4. Last part is to reflect what informations did we get from this analyse. Were we able to answer all question? Write explanation if not.

## Analyse

I work on python 3.11 using pandas and matplotlib.pyplot modules

FIrstly I import both csv files. I open first rows using .head() method and than do a initial analyse using .info() and .describe()

The species_info.csv contains following columns:
- **category** - taxonomy for each species
- **scientific_name** - scientific name for each species
- **common_names** - common names of each species
- **conservation_status** - conservation status for each species


The Observations.csv contains information from recorded sightings of different species throughout the national parks in the past 7 days. 

The columns included are:
- **scientific_name** - The scientific name of each species
- **park_name** - The name of the national park
- **observations** - The number of observations in the past 7 days

1. **What is the distribution of conservation status for species?**

      >NaN                   5633
      >
      >Species of Concern     161
      >
      >Endangered              16
      >
      >Threatened              10
      >
      >In Recovery              4
      >
      >Name: count, dtype: int64
      >conservation_status
      >
      >NaN                  97%
      >
      >Species of Concern   2,8%
      >
      >Endangered           0,27%
      >
      >Threatened           0,17%
      >
      >In Recovery          0,07%

As we can see above, 97% of data in this column contains empty values. We do not need to drop all column. The NaN values are equat to "Not covered by any form of protection or not endangered".

2. **Are certain types of species more likely to be endangered?**

>
>             category  not_protected  protected  protected in %
>  
>             Amphibian          72          7            8.86
>
>                 Bird          413         75           15.37
>
>                 Fish          115         11            8.73
>
>               Mammal          146         30           17.05
>
>       Nonvasc. Plant          328          5            1.50
>
>              Reptile           73          5            6.41
>
>       Vascular Plant         4216         46            1.08
>

As we can see big vertebrates like birds and mammals are the most endangered. Probably because they are the most studied groups of species.


3. Are the differences between species and their conservation status significant?


