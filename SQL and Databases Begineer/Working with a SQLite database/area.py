import sqlite3
conn = sqlite3.connect('factbook.db')
c = conn.cursor()
land = c.execute('select sum(area_land) from facts;').fetchall()
water = c.execute('select sum(area_water) from facts;').fetchall()
print(land[0][0]/water[0][0])