import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Ryanair_Data_300123.xlsx') 

df.head() # Quick check on how the dataset looks like
df.shape # Checking the shape of the data
df.info() # Summary information about the dataframe
df.duplicated().sum() # Counting the duplicate rows
df.drop_duplicates(inplace=True) # Dropping the duplicate rows
df.to_csv('Ryanair_Data_300123_v1.csv', index=False)