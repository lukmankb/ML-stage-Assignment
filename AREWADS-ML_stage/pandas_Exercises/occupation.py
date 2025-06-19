#Ex3 - Getting and Knowing your Data
#This time we are going to pull data directly from the internet. Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.

#tep 1. Import the necessary libraries 
import pandas as pd
#Step 2. Import the dataset from this address.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
#Step 3. Assign it to a variable called users and use the 'user_id' as index
users = pd.read_csv(url, sep='|', index_col='user_id')
#Step 4. See the first 25 entries
print(users.head(25))
#Step 5. See the last 10 entries
print(users.tail(10))
#Step 6. What is the number of observations in the dataset?
users.shape
print(f"Number of observations: {users.shape[0]}")
#Step 7. What is the number of columns in the dataset?
users.shape
print(f"Number of columns: {users.shape[1]}")
#Step 8. Print the name of all the columns.
print("Column names:", users.columns)
#Step 9. How is the dataset indexed?
print("Dataset index:", users.index)
#Step 10. What is the data type of each column?
print("Data types of each column:\n", users.dtypes)
#Step 11. Print only the occupation column
print("Occupation column:\n", users['occupation'])
#Step 12. How many different occupations are in this dataset?
unique_occupations = users['occupation'].nunique()
print(f"Number of different occupations: {unique_occupations}")
#Step 13. What is the most frequent occupation?
most_frequent_occupation = users['occupation'].mode()[0]
print(f"Most frequent occupation: {most_frequent_occupation}")
#Step 14. Summarize the DataFrame.
print("DataFrame summary:\n", users.describe(include='all'))
#Step 15. Summarize only the occupation column.
occupation_summary = users['occupation'].describe()
print("Occupation column summary:\n", occupation_summary)
#Step 16. What is the mean age of users?
mean_age = users['age'].mean()
print(f"Mean age of users: {mean_age:.2f}")
#Step 17. What is the age with least occurrence?
least_occurrence_age = users['age'].mode().iloc[0]
print(f"Age with least occurrence: {least_occurrence_age}")
