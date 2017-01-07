## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
plt.plot(unrate['DATE'].head(12),unrate['VALUE'].head(12))
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')

## 2. Matplotlib Classes ##

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 4. Adding Data ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate['DATE'].head(12),unrate['VALUE'].head(12))
ax2.plot(unrate['DATE'].iloc[12:24],unrate['VALUE'].iloc[12:24])

plt.show()

## 5. Formatting And Spacing ##

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

## 6. Comparing Across More Years ##

fig = plt.figure(figsize=(12,12))
x = [0,12,24,36,48]
y = [12,24,36,48,60]
for i in range(5):
    ax = fig.add_subplot(5,1,(i+1))
    ax.plot(unrate[x[i]:y[i]]['DATE'],unrate[x[i]:y[i]]['VALUE'])
plt.show()                 

## 7. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(6,3))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'],c='red')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'],c='blue')
plt.show()

## 8. Adding More Lines ##

fig = plt.figure(figsize=(10,6))
x = [0,12,24,36,48]
y = [12,24,36,48,60]
color = ['red','blue','green','orange','black']
for i in range(5):
    plt.plot(unrate[x[i]:y[i]]['MONTH'],unrate[x[i]:y[i]]['VALUE'],c = color[i])
plt.show()       

## 9. Adding A Legend ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']

for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    label = str(1948 + i)
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i],label=label)
plt.legend(loc='upper left')    
plt.show()

## 10. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel('Month, Integer')
plt.ylabel('Unemployment Rate, Percent')
plt.show()