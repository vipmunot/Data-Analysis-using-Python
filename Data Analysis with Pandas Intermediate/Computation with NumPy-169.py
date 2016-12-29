## 2. Array Comparisons ##

countries_canada = (world_alcohol[:,2] == 'Canada')
years_1984 = (world_alcohol[:,0] == '1984')

## 3. Selecting Elements ##

country_is_algeria = (world_alcohol[:,2] == 'Algeria')
country_algeria = world_alcohol[country_is_algeria,:]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

## 5. Replacing Values ##

world_alcohol[world_alcohol[:,0]=='1986',0] = '2014'
world_alcohol[world_alcohol[:,3]=='Wine',3] = 'Grog'

## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4]==''
world_alcohol[is_value_empty,4]='0'

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

canada_1986 = world_alcohol[(world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Canada'),:]
canada_1986[canada_1986[:,4] == '',4] = '0'
canada_alcohol = canada_1986[:,4].astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##


years = world_alcohol[:,0]
years = set(years)
countries = set(world_alcohol[:,2])
def alcohol_consumption_country_year(year):
    totals = {}
    for country in countries:
        country_consumption = world_alcohol[(world_alcohol[:,0] == year) & (world_alcohol[:,2]== country),:]
        country_consumption[country_consumption[:,4] == '',4] = '0'
        country_alcohol = country_consumption[:,4].astype(float)
        total_country_drinking = country_alcohol.sum()
        totals[country] = total_country_drinking
    return(totals)

totals = alcohol_consumption_country_year('1989')



## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for item,val in totals.items():
    if val > highest_value:
        highest_value = val
        highest_key = item