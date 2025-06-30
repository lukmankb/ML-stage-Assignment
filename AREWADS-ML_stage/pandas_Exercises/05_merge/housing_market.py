#Housing Market
#Introduction:
#This time we will create our own dataset with fictional numbers to describe a house market. As we are going to create random data don't try to reason of the numbers.

#Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
#Step 2. Create 3 differents Series, each of length 100, as follows:
#The first a random number from 1 to 4
#The second a random number from 1 to 3
#The third a random number from 10,000 to 30,000
s1 = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))
s2 = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))
s3 = pd.Series(np.random.randint(10000, high=30001, size=100, dtype='l'))

print(s1, s2, s3) 
#Step 3. Let's create a DataFrame by joinning the Series by column
housemkt = pd.concat([s1, s2, s3], axis=1)
print(housemkt.head())
#Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter
housemkt.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True)
print(housemkt.head()) 
#Step 5. Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'
bigcolumn = pd.concat([s1, s2, s3], axis=0)

# it is still a Series, so we need to transform it to a DataFrame
bigcolumn = bigcolumn.to_frame()
print(type(bigcolumn))

print(bigcolumn)
#Step 6. Oops, it seems it is going only until index 99. Is it true?
print(len(bigcolumn))

#Step 7. Reindex the DataFrame so it goes from 0 to 299
bigcolumn.reset_index(drop=True, inplace=True)
print(bigcolumn)