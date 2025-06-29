#Ex - GroupBy
#Introduction:
#GroupBy can be summarized as Split-Apply-Combine.

#Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.

#Check out this Diagram

#Step 1. Import the necessary libraries
import pandas as pd 
#Step 2. Import the dataset from this address.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
#Step 3. Assign it to a variable called drinks.
drinks = pd.read_csv(url, sep=',')
print(drinks.head())
#Step 4. Which continent drinks more beer on average?
print(drinks.groupby('continent').beer_servings.mean())
#Step 5. For each continent print the statistics for wine consumption.
print(drinks.groupby('continent').wine_servings.describe())
#Step 6. Print the mean alcohol consumption per continent for every column
mean_alcohol = drinks.groupby('continent').mean()
print(mean_alcohol)
#Step 7. Print the median alcohol consumption per continent for every column
median_alcohol = drinks.groupby('continent').median()
print(median_alcohol)
#Step 8. Print the mean, min and max values for spirit consumption.
print(drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max']))
#This time output a DataFrame
