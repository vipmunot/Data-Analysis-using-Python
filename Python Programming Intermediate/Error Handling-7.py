## 2. Sets ##

#legislators = list(csv.reader(open('legislators.csv','r')))
gender = []
for item in legislators:
    gender.append(item[3])
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

party = []
for item in legislators:
    party.append(item[6])
party = set(party)
print(party)
print(legislators)

## 4. Missing Values ##

for item in legislators:
    if item[3]=='':
        item[3]= 'M'


## 5. Parsing Birth Years ##

birth_years = []
for item in legislators:
    parts = item[2].split("-")
    birth_years.append(parts[0])

## 6. Try/except Blocks ##

try:
    float("hello")
except Exception:
    print("Error converting to float..")

## 7. Exception Instances ##

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for item in birth_years:
    try:
        item = int(item)
    except Exception:
        pass
    converted_years.append(item)

## 9. Convert Birth Years to Integers ##

for item in legislators:
    try:
        birth_year = int(item[2].split('-')[0])
    except Exception:
        birth_year = 0
    item.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value = 1
for item in legislators:
    if item[7]==0:
        item[7]=last_value
    last_value = item[7]