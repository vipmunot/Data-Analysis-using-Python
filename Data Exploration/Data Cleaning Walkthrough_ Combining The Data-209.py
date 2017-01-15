## 2. Condensing class size ##

class_size = data['class_size']
class_size = class_size[class_size['GRADE ']=='09-12']
class_size = class_size[class_size['PROGRAM TYPE']=='GEN ED']
print(class_size.head(5))

## 3. Computing average class sizes ##

import numpy
class_size = class_size.groupby("DBN").agg(numpy.mean)
class_size.reset_index(inplace=True)
data['class_size'] = class_size
print(data['class_size'].head(5))

## 4. Condensing demographics ##

data['demographics'] = data['demographics'][data['demographics']['schoolyear']==20112012]
print(data['demographics'].head(5))

## 5. Condensing graduation ##

data['graduation']= data['graduation'][(data['graduation']['Cohort']=='2006') & (data['graduation']['Demographic']=='Total Cohort')]
print(data['graduation'].head(5))

## 6. Converting AP test scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for col in cols:
    data['ap_2010'][col] = pd.to_numeric(data['ap_2010'][col], errors='coerce')
print(data['ap_2010'].head(5))    

## 8. Performing the left joins ##

combined = data["sat_results"]
combined = combined.merge(data['ap_2010'],how = 'left',on="DBN")
combined = combined.merge(data['graduation'],how = 'left',on="DBN")  
print(combined.head(2))
print(combined.shape)

## 9. Performing the inner joins ##

combined = combined.merge(data['class_size'],how = 'inner',on="DBN")
combined = combined.merge(data['demographics'],how = 'inner',on="DBN")
combined = combined.merge(data['survey'],how = 'inner',on="DBN")
combined = combined.merge(data['hs_directory'],how = 'inner',on="DBN")
print(combined.head(2))
print(combined.shape)

## 10. Filling in missing values ##

combined = combined.fillna(combined.mean())
combined = combined.fillna(0)
print(combined.head(2))

## 11. Adding a school district column ##

def extractstring(string):
    return(string[:2])
combined['school_dist']=combined['DBN'].apply(extractstring)
print(combined['school_dist'].head(5))