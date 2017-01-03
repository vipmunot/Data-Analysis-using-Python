## 1. Introduction ##

import pandas as pd
titanic_survival = pd.read_csv('titanic_survival.csv')

## 2. Finding the Missing Data ##

age = titanic_survival["age"]
print(age.loc[10:20])
age_null_true = age[pd.isnull(age)]
age_null_count = len(age_null_true)
print(age_null_count)

## 3. Whats the big deal with missing data? ##

age_is_null = pd.isnull(titanic_survival["age"])
age = titanic_survival["age"]
correct_mean_age = sum(age[~age_is_null])/len(age[~age_is_null])

## 4. Easier Ways to Do Math ##

correct_mean_age = titanic_survival["age"].mean()
correct_mean_fare = titanic_survival['fare'].mean()

## 5. Calculating Summary Statistics ##

passenger_classes = [1, 2, 3]
fares_by_class = {}
for item in passenger_classes:
    subset = titanic_survival[titanic_survival['pclass']== item]
    fares_by_class[item] = subset['fare'].mean()

## 6. Making Pivot Tables ##

passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived")
passenger_age = titanic_survival.pivot_table(index="pclass", values="age")
print(passenger_age)

## 7. More Complex Pivot Tables ##

import numpy as np
port_stats = titanic_survival.pivot_table(index="embarked",values=["survived","fare"],aggfunc=np.sum)
print(port_stats)

## 8. Drop Missing Values ##

drop_na_rows = titanic_survival.dropna(axis=0)
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(subset = ['sex','age'],axis = 0)

## 9. Using iloc to Access Rows by Position ##

# We have already sorted new_titanic_survival by age
first_five_rows = new_titanic_survival.iloc[0:5]
first_ten_rows= new_titanic_survival.iloc[0:10]
row_position_fifth = new_titanic_survival.iloc[4]
row_index_25 = new_titanic_survival.loc[25]

## 10. Using Column Indexes ##

first_row_first_column = new_titanic_survival.iloc[0,0]
all_rows_first_three_columns = new_titanic_survival.iloc[:,0:3]
row__index_83_age = new_titanic_survival.loc[83,"age"]
row_index_1000_pclass = new_titanic_survival.loc[766,"pclass"]
row_index_1100_age = new_titanic_survival.loc[1100,'age']
row_index_25_survived = new_titanic_survival.loc[25,'survived']
five_rows_three_cols = new_titanic_survival.iloc[:5,:3]

## 11. Reindexing Rows ##

titanic_reindexed = new_titanic_survival.reset_index(drop = True)
print(titanic_reindexed.iloc[:5,:3])

## 12. Apply Functions Over a DataFrame ##

def hundredth_row(column):
    hundredth_item = column.iloc[99]
    return hundredth_item

hundredth_row = titanic_survival.apply(hundredth_row)
def null_elements(column):
    return(len(column[pd.isnull(column)]))
column_null_count = titanic_survival.apply(null_elements)

## 13. Applying a Function to a Row ##

def is_minor(row):
    if row["age"] < 18:
        return "minor"
    elif row['age'] >=18:
        return "adult"
    else:
        return "unknown"

age_labels = titanic_survival.apply(is_minor, axis=1)

## 14. Calculating Survival Percentage by Age Group ##

age_group_survival = titanic_survival.pivot_table(index="age_labels",values='survived')