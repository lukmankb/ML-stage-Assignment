#Introduction:
#This time you will get data from a website.

#Step 1. Import the necessary libraries
import numpy as np
import pandas as pd
import pandas_datareader.data as web

# package for dates
import datetime as dt 
#Step 2. Create your time range (start and end variables). The start date should be 01/01/2015 and the end should today (whatever your today is).
# #Note: If you are using a Jupyter notebook, you can use the following code to get today's date:
# end = dt.datetime.now()
# # If you are using a Python script, you can use the following code to get today's date:
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

#Step 3. Get an API key for one of the APIs that are supported by Pandas Datareader, preferably for AlphaVantage.
#If you do not have an API key for any of the supported APIs, it is easiest to get one for AlphaVantage. (Note that the API key is shown directly after the signup. You do not receive it via e-mail.)

#(For a full list of the APIs that are supported by Pandas Datareader, see here. As the APIs are provided by third parties, this list may change.)
import os
os.environ['ALPHAVANTAGE_API_KEY'] = ' TT1Q16WZ4LGNH86R'
#Step 4. Use Pandas Datarader to read the daily time series for the Apple stock (ticker symbol AAPL) between 01/01/2015 and today, assign it to df_apple and print it. 
df_apple = web.DataReader("AAPL", "av-daily", start, end)
print(df_apple)
#Step 5. Add a new column "stock" to the dataframe and add the ticker symbol
# #Hint: You can use the following code to add a new column to a dataframe:
df_apple['stock'] = 'AAPL'
print(df_apple.head())  
#Step 6. Repeat the two previous steps for a few other stocks, always creating a new dataframe: Tesla, IBM and Microsoft. (Ticker symbols TSLA, IBM and MSFT.)
df_tesla = web.DataReader("TSLA", "av-daily", start, end)
df_tesla['stock'] = 'TSLA'
df_ibm = web.DataReader("IBM", "av-daily", start, end)
df_ibm['stock'] = 'IBM'
df_microsoft = web.DataReader("MSFT", "av-daily", start, end)
df_microsoft['stock'] = 'MSFT'
print(df_tesla.head())
print(df_ibm.head())
print(df_microsoft.head())
 
#Step 7. Combine the four separate dataFrames into one combined dataFrame df that holds the information for all four stocks
df = pd.concat([df_apple, df_tesla, df_ibm, df_microsoft], axis=0)
print(df.head())
#Step 8. Shift the stock column into the index (making it a multi-level index consisting of the ticker symbol and the date).
df = df.set_index(['stock', df.index])
print(df.head())

#Step 7. Create a dataFrame called vol, with the volume values.
vol = df[['volume']]
print(vol.head())
#Step 8. Aggregate the data of volume to weekly.
#Hint: Be careful to not sum data from the same week of 2015 and other years.
vol_weekly = vol.resample('W').sum()
print(vol_weekly.head())
#Step 9. Find all the volume traded in the year of 2015
vol_2015 = vol[vol.index.get_level_values(1).year == 2015]
print(vol_2015.head())
