# **Welcome to Ryanair Price analysis in Python [IN PROGRESS]**

### *Characteristics:*
* Difficulty: _Beginner/Intermediate level_
* Program Language: _Python_
* Visualization Tool: _Tableau_

***

## 1.1 Scenario

<img src="https://github.com/damicodavid/Ryanair_Price_Analysis/assets/156213397/4ca23176-7a01-4bf6-901f-739855295eb5" alt="drawing" width="300"/>


Ryanair is an airline company founded in 1985 by Irish businessman Tony Ryan.
<br>
As of today, the company boasts *565 aircraft*, *over 22,000 employees*, and transported more than *142 million people in 2022*. 
<br>It operates over 3,000 routes daily across 40 countries and 240 airports.

We gathered data through an API of these 2 route:
* Milano Maplpensa (MXP) --> Catania (CTA) - Sicily
* Milano-Bergamo (BGY) --> Catania (CTA) - Sicily

****

## 1.2 Goals Insights

1. How then company discriminate the ticket price based on the starting airport (Main - Milano Malpensa, closer to the city & Secondary - Bergamo)

2. How price differ if I need to book for a date close to the gathering date?

3. How price differ from high to low season period (Christmas holidays)?


***


## 1.3 Step-by-step Analysis 

We'll analyze data from 01/11/2023 to 24/01/2023 and we'll present our insight through a interactive dashboard.

**1. Download the public data from -> [Datasets](xxxx)**

**2. Verify how is the data organized (columns structure and wideness)?**

**3. Are there issues with bias or credibility in this data?** 

**4. Does your data ROCCC (Reliable, Original, Comprehensive, Current, Cited)?**
<br>
<br>

**After these preliminary phases we can go through the _Data overview process_:**

**5.Install through Powershell Terminal:**

``` 
pip install numpy as np
pip install numpy pandas
pip install numpy matplotlib.pyplot
pip install numpy seaborn
``` 

**6.Import libraries & Overview your data:**

``` 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Ryanair_Data_300123.xlsx') 

df.head() 

# Quick check on how the dataset looks like

```
This will give you and overview of your data:



repeat for the second dataframe
``` 
import pandas as pd

df2 = pd.read_csv("Divvy_Trips_2020_Q1.csv") 

print(df2)
```
we can notice that we have different name convetion for similar data that we'll have to rename so we can merge the two dataframe:
![image](https://github.com/damicodavid/Bycicly_Share_Project/assets/156213397/cb05e292-bf98-4403-b9bf-e8ebed549a48)
<br>
<br>

**6. Check data type of each column**

``` 
import pandas as pd

df = pd.read_csv("Divvy_Trips_2019_Q4.csv")
 
data_type= df.dtypes

print(data_type)
```
<br>
<br>

**After these overview phases we can go through the _Data manipulation and cleaning process_:**
<br>
**7.Before cleaning it's essential to merge the two data-frames verifying that the column names is unique in both file:**
```
import pandas as pd

df1 = pd.read_csv("Divvy_Trips_2019_Q4.csv") 
df2 = pd.read_csv("Divvy_Trips_2020_Q1.csv") 

print("Columns in df1:", df1.columns)
print("Columns in df2:", df2.columns)
```
we can notice that we have different columns names for data of the same category:
![image](https://github.com/damicodavid/Bycicly_Share_Project/assets/156213397/ccc0292e-ccd8-4668-832e-1e6d852d775f)
<br>
<br>
<br>

**8.Rename columns names of the second data-frame and replace value in df1 for user type in order to have standardized naming convention between the two dataset and save as a new files:**
```
import pandas as pd

df1 = pd.read_csv("Divvy_Trips_2019_Q4.csv") 
df2 = pd.read_csv("Divvy_Trips_2020_Q1.csv") 

column_name_mapping = {
    'ride_id': 'trip_id',
    'started_at': 'start_time',
    'ended_at': 'end_time',
    'start_station_name': 'from_station_name',
    'start_station_id': 'from_station_id',
    'end_station_id': 'to_station_id',
    'end_station_name': 'to_station_name',
    'member_casual': 'usertype',
    }

df2.rename(columns=column_name_mapping, inplace=True)

print("Columns in df2:", df2.columns)

column_to_modify = 'usertype'
value_mapping = {'Subscriber': 'member', 'Customer': 'casual'}


df1['usertype'] = df1['usertype'].replace(value_mapping)

column_to_convert = 'trip_id'

df1[column_to_convert] = df1[column_to_convert].astype('object')

df1.to_csv('Divvy_Trips_2019_Q4_renamed.csv', index=False)
df2.to_csv('Divvy_Trips_2020_Q1_renamed.csv', index=False)
```
File will be saved with a new name "oldnamefile_renamed"
<br>
<br>
**9.Concat the two file in a unique dataset:**

import pandas as pd

df1 = pd.read_csv("Divvy_Trips_2019_Q4_renamed.csv") 
df2 = pd.read_csv("Divvy_Trips_2020_Q1_renamed.csv") 

column_to_convert = 'trip_id'

df1[column_to_convert] = df1[column_to_convert].astype('object')

concatenated_df = pd.concat([df1, df2], axis=0)

concatenated_df.to_csv('Divvy_Trips_2019_Q4_and_2020_Q1', index=False)
<br>
<br>
**10. Remove any duplicates in the dataset and replace n/a values with "not specified" and then save:**

``` 
import pandas as pd

df = pd.read_csv("Divvy_Trips_2019_Q4_and_2020_Q1.csv") 

df = df.drop_duplicates()

df = df.fillna(value="not specified")

print(df)

df.to_csv('Divvy_Trips_2019_Q4_and_2020_Q1_v1', index=False)
```
<br>
<br>

**11. Creation of new columns such as "ride length" and "weekday" for our following analysis:**

```
import pandas as pd

df= pd.read_csv("Divvy_Trips_2019_Q4_and_2020_Q1_C") 

df['weekday'] = pd.to_datetime(df['start_time']).dt.day_name()

df['time_difference'] = pd.to_datetime(df['end_time']) - pd.to_datetime(df['start_time'])

df.to_csv('Divvy_Trips_2019_Q4_and_2020_Q1_C_v2.csv', index=False)
```

Now we have all the data we need to start to analyse and create our dashboards that we will tell our story about the dataset in order to address marketing requests.

After have been analyzed data we find out that casual riders are most likely using more bicycle in the weekends and the average ride time is almost 4 times longer than the member one.

<br>
<br>

***
## 1.4 Visualization and Conclusions

![Dashboard_Cyclist](https://github.com/damicodavid/Bycicly_Share_Project/assets/156213397/e8adf448-faa8-4eae-9d7c-1d285ae4ea92)
Check my viz here->[Tableau Pubblic](https://public.tableau.com/app/profile/david.d.amico/viz/Project_Google_17050844221870/Dashboard2)
<br>
<br>
**INSIGHTS:**
1. It seems casual riders use bicycle for leisure purpose and members as an alternative transports for daily activities (work,school...);
2. 13.68 % of the total rides is made from casual customers that could be retained as members and increase total revenues;
3. Average Age is lower for casual riders 36 vs 41 Years old for member one.

**SOLUTIONS:**
1. Increasing the percentage of members is possible through a well structured loyalty program;
2. Proposed assigning unique rider ID numbers for in-depth analysis and ensure compliance with GDPR principles in data handling;
3. Create a campaign to target younger clients to increase total revenue.
