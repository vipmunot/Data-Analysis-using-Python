## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")
unique_regions = cars['origin'].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
print(cars.head())
dummy_years = pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)
cars = cars.drop("year", axis=1)
cars = cars.drop("cylinders", axis=1)
print(cars.head())

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]
highest_train_row = int(cars.shape[0] * .70)
train = shuffled_cars.iloc[0:highest_train_row]
test = shuffled_cars.iloc[highest_train_row:]

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression
import re
unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}
X = train[[x for x in train.columns if x.startswith("cyl") or x.startswith("year")]]
print(X.shape)

for origin in unique_origins:
    y = (train["origin"] == origin)
    lr = LogisticRegression()
    lr.fit(X, y)
    models[origin] = lr

print(models)

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)
test = test[[x for x in test.columns if x.startswith("cyl") or x.startswith("year")]]
print(test.shape)
for origin in unique_origins:
    X_test = test[features]
    testing_probs[origin] = models[origin].predict_proba(X_test)[:,1]

## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis = 1)
print(predicted_origins)