#Introduction:
#This exercise was created based on the tutorial and documentation from Seaborn
#The dataset being used is tips from Seaborn.

#Step 1. Import the necessary libraries:
import pandas as pd

# visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
# set seaborn style to white
sns.set_style("white")
#Step 2. Import the dataset from this address.
#Step 3. Assign it to a variable called tips
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Tips/tips.csv'
tips = pd.read_csv(url)

print(tips.head()) 
#Step 4. Delete the Unnamed 0 column
del tips['Unnamed: 0']

tips.head()
#Step 5. Plot the total_bill column histogram
# create histogram
ttbill = sns.distplot(tips.total_bill);

# set lables and titles
ttbill.set(xlabel = 'Value', ylabel = 'Frequency', title = "Total Bill")

# take out the right and upper borders
sns.despine() 
#Step 6. Create a scatter plot presenting the relationship between total_bill and tip
sns.jointplot(x ="total_bill", y ="tip", data = tips) 
#Step 7. Create one image with the relationship of total_bill, tip and size.
#Hint: It is just one function.
sns.pairplot(tips) 
#Step 8. Present the relationship between days and total_bill value
sns.stripplot(x = "day", y = "total_bill", data = tips, jitter = True); 
#Step 9. Create a scatter plot with the day as the y-axis and tip as the x-axis, differ the dots by sex
sns.stripplot(x = "tip", y = "day", hue = "sex", data = tips, jitter = True);
#Step 10. Create a box plot presenting the total_bill per day differetiation the time (Dinner or Lunch)
sns.boxplot(x = "day", y = "total_bill", hue = "time", data = tips, palette = "Set3");
#Step 11. Create two histograms of the tip value based for Dinner and Lunch. They must be side by side.
# better seaborn style
sns.set(style = "ticks")

# creates FacetGrid
g = sns.FacetGrid(tips, col = "time")
g.map(plt.hist, "tip"); 
#Step 12. Create two scatterplots graphs, one for Male and another for Female, presenting the total_bill value and tip relationship, differing by smoker or no smoker
#They must be side by side.
g = sns.FacetGrid(tips, col = "sex", hue = "smoker")
g.map(plt.scatter, "total_bill", "tip", alpha =.7)

g.add_legend();
 
g = sns.FacetGrid(tips, col = "sex", hue = "smoker")
g.map(plt.scatter, "total_bill", "tip", alpha =.7)

g.add_legend();
 
#BONUS: Create your own question and answer it using a graph.
 