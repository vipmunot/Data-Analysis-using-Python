## 3. Exploring the data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filter out the bad years ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers['Year']>1959]

## 5. Consolidating deaths ##

def count_deaths(row):
    num_deaths = 0
    columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    
    for c in columns:
        death = row[c]
        if pd.isnull(death) or death == 'NO':
            continue
        elif death == 'YES':
            num_deaths += 1
    return num_deaths

true_avengers['Deaths']= true_avengers.apply(count_deaths,axis = 1)
    

## 6. Years since joining ##

joined_accuracy_count  = int()
joined_accuracy_count = 2015 - true_avengers['Year']