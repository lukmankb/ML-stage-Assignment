#Regiment
#Introduction:
#Special thanks to: http://chrisalbon.com/ for sharing the dataset and materials.

#Step 1. Import the necessary libraries
import pandas as pd
import numpy as np 
#Step 2. Create the DataFrame with the following values:
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
#Step 3. Assign it to a variable called regiment.
regiment = pd.DataFrame(raw_data, columns = raw_data.keys())
print(regiment)

#Don't forget to name each column
 
#Step 4. What is the mean preTestScore from the regiment Nighthawks?
print("Mean preTestScore for Nighthawks:", regiment[regiment['regiment'] == 'Nighthawks']['preTestScore'].mean())
#Step 5. Present general statistics by company
print("General statistics by company:\n", regiment.groupby('company').describe()) 
#Step 6. What is the mean of each company's preTestScore?
print("Mean preTestScore by company:\n", regiment.groupby('company')['preTestScore'].mean()) 
#Step 7. Present the mean preTestScores grouped by regiment and company
print("Mean preTestScores grouped by regiment and company:\n", 
      regiment.groupby(['regiment', 'company'])['preTestScore'].mean().reset_index()) 
#Step 8. Present the mean preTestScores grouped by regiment and company without heirarchical indexing
print("Mean preTestScores grouped by regiment and company without heirarchical indexing:\n", 
      regiment.groupby(['regiment', 'company'], as_index=False)['preTestScore'].mean()) 
#Step 9. Group the entire dataframe by regiment and company
print("Grouped DataFrame by regiment and company:\n", 
      regiment.groupby(['regiment', 'company']).mean().reset_index()) 
#Step 10. What is the number of observations in each regiment and company
print("Number of observations in each regiment and company:\n", 
      regiment.groupby(['regiment', 'company']).size().reset_index(name='observations')) 
#Step 11. Iterate over a group and print the name and the whole data from the regiment
# Group the dataframe by regiment, and for each regiment,
for name, group in regiment.groupby('regiment'):
    # print the name of the regiment
    print(name)
    # print the data of that regiment
    print(group) 