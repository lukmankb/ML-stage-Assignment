#Fictitious Names
#Introduction:
#This time you will create a data again

#Special thanks to Chris Albon for sharing the dataset and materials. All the credits to this exercise belongs to him.

#In order to understand about it go here.

#Step 1. Import the necessary libraries
import pandas as pd
import numpy as np 
#Step 2. Create the 3 DataFrames based on the following raw data
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
#Step 3. Assign each to a variable called data1, data2, data3
data1 = pd.DataFrame(raw_data_1, columns = ['subject_id', 'first_name', 'last_name'])
data2 = pd.DataFrame(raw_data_2, columns = ['subject_id', 'first_name', 'last_name'])
data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])

print(data3) 
#Step 4. Join the two dataframes along rows and assign all_data
all_data = pd.concat([data1, data2])
print(all_data) 
#Step 5. Join the two dataframes along columns and assing to all_data_col
all_data_col = pd.concat([data1, data2], axis = 1)
print(all_data_col) 
#Step 6. Print data3
print(data3) 
#Step 7. Merge all_data and data3 along the subject_id value
print(pd.merge(all_data, data3, on='subject_id')) 
#Step 8. Merge only the data that has the same 'subject_id' on both data1 and data2
print(pd.merge(data1, data2, on='subject_id', how='inner'))
#Step 9. Merge all values in data1 and data2, with matching records from both sides where available.
print(pd.merge(data1, data2, on='subject_id', how='outer')) 