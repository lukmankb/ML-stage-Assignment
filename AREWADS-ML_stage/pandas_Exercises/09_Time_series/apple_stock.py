#Introduction:
#We are going to use Apple's stock price.

#Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

# visualization
import matplotlib.pyplot as plt 
#Step 2. Import the dataset from this address

#Step 3. Assign it to a variable apple
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple = pd.read_csv(url)

print(apple.head()) 
#Step 4. Check out the type of the columns
print(apple.dtypes) 
#Step 5. Transform the Date column as a datetime type
apple.Date = pd.to_datetime(apple.Date)

print(apple['Date'].head()) 
#Step 6. Set the date as the index
apple = apple.set_index('Date')

print(apple.head()) 
#Step 7. Is there any duplicate dates?
print(apple.index.is_unique) 
#Step 8. Ops...it seems the index is from the most recent date. Make the first entry the oldest date.
print(apple.sort_index(ascending = True).head())
#Step 9. Get the last business day of each month
apple_month = apple.resample('BME').mean()

print(apple_month.head()) 
#Step 10. What is the difference in days between the first day and the oldest
print((apple.index.max() - apple.index.min()).days) 
#Step 11. How many months in the data we have?
apple_months = apple.resample('BME').mean()

print(len(apple_months.index)) 
#Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
appl_open = apple['Adj Close'].plot(title = "Apple Stock")

# changes the size of the graph
fig = appl_open.get_figure()
fig.set_size_inches(13.5, 9) 
plt.show()
#BONUS: Create your own question and answer it.
 