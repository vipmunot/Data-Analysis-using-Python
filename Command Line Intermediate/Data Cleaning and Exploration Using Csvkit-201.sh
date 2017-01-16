## 2. Csvstack ##

/home/dq$ head Combined_huds.csv

## 3. Csvlook ##

/home/dq$ head -10 Combined_huds.csv | csvlook

## 4. Csvcut ##

/home/dq$ csvcut -c 2 Combined_huds.csv | head -10

## 5. Csvstat ##

3511/home/dq$ csvstat Combined_huds.csv

## 6. Csvcut | csvstat ##

/home/dq$ csvcut -c 2 Combined_huds.csv | csvstat

## 7. Csvgrep ##

/home/dq$ csvgrep -c 2 -m -9 Combined_huds.csv | head -10 | csvlook

## 8. Filtering out problematic rows ##

/home/dq$ csvgrep -c 2 -m -9 -i Combined_huds.csv > positive_ages_only.csv