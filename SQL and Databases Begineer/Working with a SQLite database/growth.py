import sqlite3
conn = sqlite3.connect('factbook.db')
import pandas as pd
import math
df = pd.read_sql_query('select * from facts;', conn)
conn.close()
print(df.shape)
df = df.dropna()
print(df.shape)
def growth(population,growth_rate):
    N = population * pow(math.e,(growth_rate /100)*35)
    return N
pop = []
for index,row in df.iterrows():
    pop.append(growth(row['population'],row['population_growth']))
df['2050_population'] = pop
pop_2050 = df.sort_values(by='2050_population', ascending=0)
print(df.sort_values(by='2050_population', ascending=0)[:10])