# **Welcome to Ryanair Price analysis in Python**

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

We gathered data through an API of these 2 routes:
* Milano Maplpensa (MXP) --> Catania (CTA) - Sicily
* Milano-Bergamo (BGY) --> Catania (CTA) - Sicily

****

## 1.2 Goals Insights

* How company discriminate the ticket price based on the starting airport (Main - Milano Malpensa, closer to the city & Secondary - Bergamo)

* How does the ticket price change as we move further away from today's date and book with less advance notice??

* How price differ from high to low season period (Ex: Christmas holidays)?


***
We'll analyze data from 01/11/2023 to 24/01/2023 and we'll present our insight through a interactive dashboard.

## 1.3 Step-by-step Analysis 

**1. Download the public data from -> [Datasets](https://github.com/damicodavid/Ryanair_Price_Analysis-In-progress-/blob/main/Ryanair_Data_300123.xlsx)**

**2. Verify how is the data organized (columns structure and wideness)?**

**3. Are there issues with bias or credibility in this data?** 

**4. Does your data ROCCC (Reliable, Original, Comprehensive, Current, Cited)?**
<br>
<br>

### Data overview process:

**5. Install Packages on Python by Powershell Terminal:**

``` 
pip install numpy as np
pip install numpy pandas
pip install numpy matplotlib.pyplot
pip install numpy seaborn
``` 

**6. Import libraries & Overview your data:**

``` 
import pandas as pd

df = pd.read_excel('Ryanair_Data_300123.xlsx') 

df.head() # Quick check on how the dataset looks like
df.shape # Checking the shape of the data

```
This will give you and overview of your data:

![1 Overview Data](https://github.com/damicodavid/Ryanair_Price_Analysis-In-progress-/assets/156213397/37f93c89-eda2-4814-8643-1552cbed74bc)

**7. Check data type and other crucial info of each column:**

``` 
import pandas as pd

df = pd.read_csv("Divvy_Trips_2019_Q4.csv")
 
df.info() # Summary information about the dataframe

```

***

### Data manipulation and cleaning process:

**8.Check and remove any duplicates:**
```
import pandas as pd

df = pd.read_excel('Ryanair_Data_300123.xlsx') 

df.head() # Quick check on how the dataset looks like
df.shape # Checking the shape of the data
df.info() # Summary information about the dataframe
df.duplicated().sum() # Counting the duplicate rows
df.drop_duplicates(inplace=True) # Dropping the duplicate rows
df.to_csv('Ryanair_Data_300123_v1.csv', index=False)

```
<br>

Now that we have all the data we'll start the analysis process and then create the dashboards that will endorse our conlusions.

<br>

***
## 1.4 Visualization and Conclusions

![Dashboard_Ryanair_v1](https://github.com/damicodavid/Ryanair_Price_Analysis-In-progress-/assets/156213397/8278e175-5de4-4879-bc67-f0b90aca2411)


Check my viz here->[Tableau Pubblic](https://public.tableau.com/app/profile/david.d.amico/viz/Ryanair_Analysis/Dashboard1)
<br>
<br>
**INSIGHTS:**
1. Prices during Christmas season skyrocket around 500% more than the average price.
2. Booking with at least 3 days prior we can save 71% in ticket price.
3. Tuesday and Wednesday seems the cheapest days to fly.
