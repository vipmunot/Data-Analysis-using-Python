## 4. Reading in the data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for f in data_files:
    d = pd.read_csv("schools/{0}".format(f))
    key_name = f.replace(".csv", "")
    data[key_name] = d

## 5. Exploring the SAT data ##

print(data['sat_results'].head(5))

## 6. Exploring the other data ##

for key in data:
    print(data[key].head(5))

## 7. Reading in the survey data ##

all_survey = pd.read_csv('schools/survey_all.txt',delimiter='\t',encoding='windows-1252')
d75_survey = pd.read_csv('schools/survey_d75.txt',delimiter='\t',encoding='windows-1252')
survey = pd.concat([all_survey,d75_survey],axis=0)
survey.head(5)

## 8. Cleaning up the surveys ##

survey['DBN']=survey['dbn']
cols = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey = survey[cols]
data['survey']=survey
data['survey'].shape

## 9. Inserting DBN fields ##

data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

def pad_csd(num):
    string_representation = str(num)
    if len(string_representation) > 1:
        return string_representation
    else:
        return string_representation.zfill(2)
    
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]
print(data["class_size"].head())

## 10. Combining the SAT scores ##

['cols = [\'SAT Math Avg. Score\', \'SAT Critical Reading Avg. Score\', \'SAT Writing Avg. Score\']\nfor c in cols:\n    data["sat_results"][c] = pd.to_numeric(data["sat_results"][c], errors="coerce")\n\ndata[\'sat_results\'][\'sat_score\'] = data[\'sat_results\'][cols[0]] + data[\'sat_results\'][cols[1]] + data[\'sat_results\'][cols[2]]\nprint(data[\'sat_results\'][\'sat_score\'].head())']

## 12. Extracting the longitude ##

import re
def find_long(loc):
    coords = re.findall("\(.+, .+\)", loc)
    long = coords[0].split(",")[1].replace(")", "")
    return long
data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(find_long)
cols = ['lon','lat']
for c in cols:
    data["hs_directory"][c] = pd.to_numeric(data["hs_directory"][c], errors="coerce")
print(data['hs_directory'].head(5))