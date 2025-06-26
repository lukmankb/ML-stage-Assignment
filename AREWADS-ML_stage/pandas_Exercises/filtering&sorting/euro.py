#Ex2 - Filtering and Sorting Data
#This time we are going to pull data directly from the internet.

#Step 1. Import the necessary libraries
import pandas as pd 
#Step 2. Import the dataset from this address.
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
#Step 3. Assign it to a variable called euro12.
euro12 = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv', sep=',')
 
#Step 4. Select only the Goal column.
euro12_goals = euro12[['Team', 'Goals']]
print("Goals column:\n", euro12_goals) 
#Step 5. How many team participated in the Euro2012?
num_teams = euro12.shape[0]
print(f"Number of teams that participated in Euro 2012: {num_teams}")
#Step 6. What is the number of columns in the dataset?
print(euro12.info())
#Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline) 
#Step 8. Sort the teams by Red Cards, then to Yellow Cards
discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False) 
#Step 9. Calculate the mean Yellow Cards given per Team
mean_yellow_cards = euro12['Yellow Cards'].mean()
print(f"Mean Yellow Cards per Team: {mean_yellow_cards:.2f}")
#Step 10. Filter teams that scored more than 6 goals
more_than_6_goals = euro12[euro12['Goals'] > 6]
print("Teams that scored more than 6 goals:\n", more_than_6_goals) 
#Step 11. Select the teams that start with G
print(euro12[euro12.Team.str.startswith('G')]) 
#Step 12. Select the first 7 columns
print(euro12.iloc[: , 0:7]) 
#Step 13. Select all columns except the last 3.
print(euro12.iloc[: , :-3]) 
#Step 14. Present only the Shooting Accuracy from England, Italy and Russia
print(euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]) 