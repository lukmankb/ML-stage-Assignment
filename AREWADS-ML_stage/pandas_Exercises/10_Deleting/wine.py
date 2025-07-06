#Introduction:
#This exercise is a adaptation from the UCI Wine dataset. The only pupose is to practice deleting data with pandas.

#Step 1. Import the necessary libraries
import pandas as pd
import numpy as np 
#Step 2. Import the dataset from this address.
#Step 3. Assign it to a variable called wine
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
wine = pd.read_csv(url)

print(wine.head()) 
#Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns
wine = wine.drop(wine.columns[[0,3,6,8,11,12,13]], axis = 1)

print(wine.head()) 
#Step 5. Assign the columns as below:
#The attributes are (donated by Riccardo Leardi, riclea '@' anchem.unige.it):

#alcohol
#malic_acid
#alcalinity_of_ash
#magnesium
#flavanoids
#proanthocyanins
#hue
wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']
print(wine.head()) 
#Step 6. Set the values of the first 3 rows from alcohol as NaN
wine.iloc[0:3, 0] = np.nan
print(wine.head()) 
#Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN
wine.iloc[2:4, 3] = np.nan
print(wine.head()) 
#Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium
wine.alcohol.fillna(10, inplace = True)

wine.magnesium.fillna(100, inplace = True)

print(wine.head()) 
#Step 9. Count the number of missing values
print(wine.isnull().sum()) 
#Step 10. Create an array of 10 random numbers up until 10
random = np.random.randint(10, size = 10)
print(random) 
#Step 11. Use random numbers you generated as an index and assign NaN value to each of cell.
wine.alcohol[random] = np.nan
print(wine.head(10)) 
#Step 12. How many missing values do we have?
print(wine.isnull().sum())
#Step 13. Delete the rows that contain missing values
wine = wine.dropna(axis = 0, how = "any")
print(wine.head()) 
#Step 14. Print only the non-null values in alcohol
mask = wine.alcohol.notnull()
print(mask) 
#Step 15. Reset the index, so it starts with 0 again
wine = wine.reset_index(drop = True)
print(wine.head())
#BONUS: Create your own question and answer it.
 