#US - Baby Names
#Introduction:
#We are going to use a subset of US Baby Names from Kaggle.
#In the file it will be names from 2004 until 2014

#Step 1. Import the necessary libraries
import pandas as pd
import numpy as np 
#Step 2. Import the dataset from this address.
#Step 3. Assign it to a variable called baby_names.
baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
baby_names.info() 
#Step 4. See the first 10 entries
print(baby_names.head(10))
#Step 5. Delete the column 'Unnamed: 0' and 'Id'
del baby_names['Unnamed: 0']

# deletes Unnamed: 0
del baby_names['Id']

print(baby_names.head())
 
#Step 6. Is there more male or female names in the dataset?
print(baby_names['Gender'].value_counts())
#Step 7. Group the dataset by name and assign to names
del baby_names["Year"]

# group the data
names = baby_names.groupby("Name").sum()

# print the first 5 observations
names.head()

# print the size of the dataset
print(names.shape)

# sort it from the biggest value to the smallest one
print(names.sort_values("Count", ascending = 0).head()) 
#Step 8. How many different names exist in the dataset?
print(len(names)) 
#Step 9. What is the name with most occurrences?
print(names.Count.idxmax()) 
#Step 10. How many different names have the least occurrences?
print(len(names[names.Count == names.Count.min()])) 
#Step 11. What is the median name occurrence?
print(names[names.Count == names.Count.median()]) 
#Step 12. What is the standard deviation of names?
print(names.Count.std()) 
#Step 13. Get a summary with the mean, min, max, std and quartiles.
print(names.describe())
 