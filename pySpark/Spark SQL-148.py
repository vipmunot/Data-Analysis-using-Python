## 4. Filtering ##

query = 'select males, females from census2010 where age>5 and age<15'
sqlCtx.sql(query).show()

## 5. Mixing Functionality ##

query = 'select males,females from census2010'
sqlCtx.sql(query).describe().show()

## 6. Multiple tables ##


from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')

census1980 = sqlCtx.read.json("census_1980.json")

census1990 = sqlCtx.read.json("census_1990.json")


census2000 = sqlCtx.read.json("census_2000.json")

tables = sqlCtx.tableNames()
print(tables)

## 7. Joins ##

query = """
 select census2010.total, census2000.total
 from census2010
 inner join census2000
 on census2010.age=census2000.age
"""

sqlCtx.sql(query).show()

## 8. SQL Functions ##

query = """
 select sum(census2010.total), sum(census2000.total), sum(census1990.total)
 from census2010
 inner join census2000
 on census2010.age=census2000.age
 inner join census1990
 on census2010.age=census1990.age
"""
sqlCtx.sql(query).show()