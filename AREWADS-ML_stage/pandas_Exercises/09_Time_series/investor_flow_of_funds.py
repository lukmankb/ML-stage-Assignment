#Introduction:
#Special thanks to: https://github.com/rgrp for sharing the dataset.

#Step 1. Import the necessary libraries
import pandas as pd 
#Step 2. Import the dataset from this address.
#Step 3. Assign it to a variable called
url = 'https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv'
df = pd.read_csv(url)
print(df.head())
#Step 4. What is the frequency of the dataset?
 
#Step 5. Set the column Date as the index.
df = df.set_index('Date')
print(df.head())
#Step 6. What is the type of the index?
print(df.index) 
#Step 7. Set the index to a DatetimeIndex type
df.index = pd.to_datetime(df.index)
print(type(df.index)) 
#Step 8. Change the frequency to monthly, sum the values and assign it to monthly.
monthly = df.resample('M').sum()
print(monthly) 
#Step 9. You will notice that it filled the dataFrame with months that don't have any data with NaN. Let's drop these rows.
monthly = monthly.dropna()
print(monthly) 
#Step 10. Good, now we have the monthly data. Now change the frequency to year.
year = monthly.resample('AS-JAN').sum()
print(year)
#BONUS: Create your own question and answer it.
 