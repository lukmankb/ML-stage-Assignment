#United States - Crime Rates - 1960 - 2014
#Introduction:
#This time you will create a data

#Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.

#Step 1. Import the necessary libraries
import pandas as pd

#Step 2. Import the dataset from this address.
#Step 3. Assign it to a variable called crime.
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)
print(crime.head())
#Step 4. What is the type of the columns?
print(crime.info())
#Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's see it now.
#Step 5. Convert the type of the column Year to datetime64
crime.Year = pd.to_datetime(crime.Year, format='%Y')
print(crime.info())
#Step 6. Set the Year column as the index of the dataframe
crime = crime.set_index('Year', drop = True)
print(crime.head())
#Step 7. Delete the Total column
del crime['Total']
print(crime.head())
#Step 8. Group the year by decades and sum the values
#Pay attention to the Population column number, summing this column is a mistake
crimes = crime.resample('10AS').sum()

# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10AS').max()

# Updating the "Population" column
crimes['Population'] = population

print(crimes)

#Step 9. What is the most dangerous decade to live in the US?
print(crime.idxmax(0)) 