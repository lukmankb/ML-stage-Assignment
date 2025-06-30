#Student Alcohol Consumption
#Introduction:
#This time you will download a dataset from the UCI.

#Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
#Step 2. Import the dataset from this address.
#Step 3. Assign it to a variable called df.
csv_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(csv_url)
print(df.head()) 
#Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
stud_alcoh = df.loc[: , "school":"guardian"]
stud_alcoh.head()
#Step 5. Create a lambda function that will capitalize strings.
capitalizer = lambda x: x.capitalize()
#Step 6. Capitalize both Mjob and Fjob
print(stud_alcoh['Mjob'].apply(capitalizer))
print(stud_alcoh['Fjob'].apply(capitalizer))
#Step 7. Print the last elements of the data set.
print(stud_alcoh.tail())
#Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.
stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'] = stud_alcoh['Fjob'].apply(capitalizer)
print(stud_alcoh.tail()) 
#Step 9. Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)
def majority(x):
    if x > 17:
        return True
    else:
        return False
stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)
print(stud_alcoh.head()) 
 
#Step 10. Multiply every number of the dataset by 10.
#I know this makes no sense, don't forget it is just an exercise
def times10(x):
    if type(x) is int:
        return 10 * x
    return x
print(stud_alcoh.applymap(times10).head(10))
 
 