#Exercise 1
#Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-facts/data
#Step 2. Download the dataset to your computer and unzip it.
import pandas as pd

#Step 3. Use the tsv file and assign it to a dataframe called food
food = pd.read_csv(r"C:\Users\user\Downloads\archive\en.openfoodfacts.org.products.tsv", sep='\t', encoding='utf-8')
#Step 4. See the first 5 entries
food.head() 
print(food.head())
#Step 5. What is the number of observations in the dataset?
print("Number of observations:", food.shape[0])
#Step 6. What is the number of columns in the dataset?
food.shape
print(food.shape[1])   
#Step 7. Print the name of all the columns.
print(food.columns)
#Step 8. What is the name of 105th column?
print(food.columns[104])   
#Step 9. What is the type of the observations of the 105th column?
print(food[food.columns[104]].dtype) 
#Step 10. How is the dataset indexed?
print(food.index)
#Step 11. What is the product name of the 19th observation?
print(food.iloc[18]['product_name'])   