## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
averages = "select avg(population), avg(population_growth), avg(birth_rate), avg(death_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_growth_avg = avg_results[0][1]
birth_rate_avg = avg_results[0][2]
death_rate_avg = avg_results[0][3]

## 2. Ranges ##

conn = sqlite3.connect("factbook.db")

averages = "select avg(population), avg(population_growth), avg(birth_rate), avg(death_rate), avg(migration_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_growth_avg = avg_results[0][1]
birth_rate_avg = avg_results[0][2]
death_rate_avg = avg_results[0][3]
mig_rate_avg = avg_results[0][4]
min_max = "select min(population), max(population), min(population_growth),max(population_growth), min(birth_rate),max(birth_rate), min(death_rate),max(death_rate) from facts;"
min_max_results = conn.execute(min_max).fetchall()
pop_min = min_max_results[0][0]
pop_max = min_max_results[0][1]
pop_growth_min = min_max_results[0][2]
pop_growth_max = min_max_results[0][3]
birth_rate_min = min_max_results[0][4]
birth_rate_max = min_max_results[0][5]
death_rate_min = min_max_results[0][6]
death_rate_max = min_max_results[0][7]
print(min_max_results)

## 3. Filtering ##

conn = sqlite3.connect("factbook.db")
min_max = "select min(population), max(population), min(population_growth), max(population_growth),min(birth_rate), max(birth_rate), min(death_rate), max(death_rate) from facts where population > 0 and population < 2000000000;"
min_max_results = conn.execute(min_max).fetchall()
pop_min = min_max_results[0][0]
pop_max = min_max_results[0][1]
pop_growth_min = min_max_results[0][2]
pop_growth_max = min_max_results[0][3]
birth_rate_min = min_max_results[0][4]
birth_rate_max = min_max_results[0][5]
death_rate_min = min_max_results[0][6]
death_rate_max = min_max_results[0][7]
print(min_max_results)

## 4. Predicting future population growth ##

import sqlite3
conn = sqlite3.connect("factbook.db")
projected_population_query = '''
select round(population + population * (population_growth/100), 0) from facts
where population > 0 and population < 7000000000 
and population is not null and population_growth is not null;
'''

projected_population = conn.execute(projected_population_query).fetchall()

print(projected_population[0:10])

## 5. Exploring projected population ##

import sqlite3
conn = sqlite3.connect("factbook.db")
proj_pop_query = '''
select round(min(population + population * (population_growth/100)), 0), 
round(max(population + population * (population_growth/100)), 0), 
round(avg(population + population * (population_growth/100)), 0)
from facts 
where population > 0 and population < 7000000000 and 
population is not null and population_growth is not null;
'''

proj_results = conn.execute(proj_pop_query).fetchall()

pop_proj_min = proj_results[0][0]
pop_proj_max = proj_results[0][1]
pop_proj_avg = proj_results[0][2]

print("Projected Population,", "Minimum: ", pop_proj_min)
print("Projected Population,", "Maximum: ", pop_proj_max)
print("Projected Population,", "Average: ", pop_proj_avg)