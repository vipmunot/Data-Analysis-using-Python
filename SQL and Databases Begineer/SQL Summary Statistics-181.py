## 1. Counting in Python ##

import sqlite3
conn = sqlite3.connect('factbook.db')
facts = conn.cursor().execute('select * from facts;').fetchall()
print(facts)
facts_count = len(facts)

## 2. Counting in SQL ##

conn = sqlite3.connect("factbook.db")
birth_rate_count = conn.cursor().execute('select count(birth_rate) from facts;').fetchall()
print(birth_rate_count)

## 3. Min and max in SQL ##

conn = sqlite3.connect("factbook.db")
min_population_growth = conn.cursor().execute('select min(population_growth) from facts;').fetchall()
print(min_population_growth)
max_death_rate = conn.cursor().execute('select max(death_rate) from facts;').fetchall()
print(max_death_rate)


## 4. Sum and average in SQL ##

conn = sqlite3.connect("factbook.db")
total_land_area = conn.cursor().execute('select sum(area_land) from facts;').fetchall()
print(total_land_area)
avg_water_area = conn.cursor().execute('select avg(area_water) from facts;').fetchall()
print(avg_water_area)

## 5. Multiple aggregation functions ##

conn = sqlite3.connect("factbook.db")
facts_stats = conn.cursor().execute('select avg(population),sum(population),max(birth_rate) from facts;').fetchall()
print(facts_stats)

## 6. Conditional aggregation ##

conn = sqlite3.connect("factbook.db")
population_growth = conn.cursor().execute('select avg(population_growth) from facts where population > 10000000;').fetchall()
print(population_growth)

## 7. Selecting unique rows ##

conn = sqlite3.connect("factbook.db")
unique_birth_rates = conn.cursor().execute('select distinct birth_rate from facts;').fetchall()
print(unique_birth_rates)

## 8. Distinct aggregations ##

conn = sqlite3.connect("factbook.db")
average_birth_rate = conn.cursor().execute('select avg(distinct birth_rate) from facts where population > 20000000;').fetchall()
print(average_birth_rate)
sum_population = conn.cursor().execute('select sum(distinct population) from facts where area_land > 1000000;').fetchall()
print(sum_population)

## 9. Arithmetic in SQL ##

conn = sqlite3.connect("factbook.db")
population_growth_millions = conn.cursor().execute('select population_growth/1000000.0  from facts;').fetchall()
print(population_growth_millions)

## 10. Arithmetic between columns ##

conn = sqlite3.connect("factbook.db")
next_year_population = conn.cursor().execute('select population + (population_growth*population)  from facts;').fetchall()
print(next_year_population)