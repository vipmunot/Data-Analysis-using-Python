## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")
fig = plt.figure(figsize=(5,12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)
ax4.set_xlim(0,5.0)

movie_reviews["RT_user_norm"].hist(ax=ax1)
movie_reviews["Metacritic_user_nom"].hist(ax=ax2)
movie_reviews["Fandango_Ratingvalue"].hist(ax=ax3)
movie_reviews["IMDB_norm"].hist(ax=ax4)

## 2. Mean ##

def calc_mean(data):
    data = data.values
    m = sum(data)/len(data)
    return(m)
user_reviews = movie_reviews[['RT_user_norm','Metacritic_user_nom','Fandango_Ratingvalue','IMDB_norm']]
reviews = user_reviews.apply(calc_mean)
rt_mean = reviews['RT_user_norm']
mc_mean = reviews["Metacritic_user_nom"]
fg_mean = reviews["Fandango_Ratingvalue"]
id_mean = reviews["IMDB_norm"]

print("Rotten Tomatoes (mean):", rt_mean)
print("Metacritic (mean):", mc_mean)
print("Fandango (mean):",fg_mean)
print("IMDB (mean):",id_mean)

## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean
def calc_variance(series):
    vals = series.values
    mean = sum(vals)/len(vals)
    v = [(i-mean)**2 for i in vals]
    v = sum(v)/len(v)
    return(v)

def calc_std(v):
    return(v**(1/2))
mean_reviews = user_reviews.apply(calc_mean)
var_reviews = user_reviews.apply(calc_variance)
std_reviews = var_reviews.apply(calc_std)
rt_var = var_reviews['RT_user_norm']
mc_var = var_reviews["Metacritic_user_nom"]
fg_var = var_reviews["Fandango_Ratingvalue"]
id_var = var_reviews["IMDB_norm"]
rt_stdev = std_reviews['RT_user_norm']
mc_stdev = std_reviews["Metacritic_user_nom"]
fg_stdev = std_reviews["Fandango_Ratingvalue"]
id_stdev = std_reviews["IMDB_norm"]
print("Rotten Tomatoes (mean):", rt_mean)
print("Metacritic (mean):", mc_mean)
print("Fandango (mean):",fg_mean)
print("IMDB (mean):",id_mean)
print("Rotten Tomatoes (variance):", rt_var)
print("Metacritic (variance):", mc_var)
print("Fandango (variance):",fg_var)
print("IMDB (variance):",id_var)
print("Rotten Tomatoes (Standard Deviation):", rt_stdev)
print("Metacritic (Standard Deviation):", mc_stdev)
print("Fandango (Standard Deviation):",fg_stdev)
print("IMDB (Standard Deviation):",id_stdev)

## 4. Scatter plots ##

fig = plt.figure(figsize=(4,8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)

ax1.scatter(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
ax2.scatter(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
ax3.scatter(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean
def calc_covariance(x,y):
    x_mean = calc_mean(x)
    y_mean = calc_mean(y)
    xval = [(i-x_mean) for i in x]
    yval = [(i-y_mean) for i in y]
    codeviates = [xval[i] * yval[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

rt_fg_covar = calc_covariance(movie_reviews['RT_user_norm'],movie_reviews['Fandango_Ratingvalue'])
mc_fg_covar = calc_covariance(movie_reviews['Metacritic_user_nom'],movie_reviews['Fandango_Ratingvalue'])
id_fg_covar = calc_covariance(movie_reviews['IMDB_norm'],movie_reviews['Fandango_Ratingvalue'])
print("Covariance between Rotten Tomatoes and Fandango:", rt_fg_covar)
print("Covariance between Metacritic and Fandango", mc_fg_covar)
print("Covariance between IMDB and Fandango", id_fg_covar)    

## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)
def calc_correlation(s1,s2):
    co = calc_covariance(s1,s2)
    std1 = calc_variance(s1)**(1/2)
    std2 = calc_variance(s2)**(1/2)
    return (co/(std1*std2))

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("Correlation between Rotten Tomatoes and Fandango:", rt_fg_covar)
print("Correlation between Metacritic and Fandango", mc_fg_covar)
print("Correlation between IMDB and Fandango", id_fg_covar)    