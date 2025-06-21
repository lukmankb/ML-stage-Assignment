#Ex1 - Filtering and Sorting Data
#This time we are going to pull data directly from the internet. Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.

#Step 1. Import the necessary libraries
import pandas as pd  
#Step 2. Import the dataset from this address.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
#Step 3. Assign it to a variable called chipo.
chipo = pd.read_csv(url, sep='\t')
#Step 4. How many products cost more than $10.00?
#Count the number of items with price greater than $10.00
expensive_items = chipo[chipo['item_price'].str.replace('$', '').astype(float) > 10.00]
print("Number of items that cost more than $10.00:", expensive_items.shape[0])
#Step 5. What is the price of each item?
#print a data frame with only two columns item_name and item_price
item_price = chipo[['item_name', 'item_price']]
item_price['item_price'] = item_price['item_price'].str.replace('$', '').astype(float)
print("Price of each item:\n", item_price)
#Step 6. Sort by the name of the item
sorted_items = chipo.sort_values(by='item_name')
print("Items sorted by name:\n", sorted_items[['item_name', 'item_price']])

#Step 7. What was the quantity of the most expensive item ordered?
# Find the most expensive item and its quantity
most_expensive_item = chipo[chipo['item_price'].str.replace('$', '').astype(float) == chipo['item_price'].str.replace('$', '').astype(float).max()]
most_expensive_quantity = most_expensive_item['quantity'].sum()
print("Quantity of the most expensive item ordered:", most_expensive_quantity)

#Step 8. How many times was a Veggie Salad Bowl ordered?
veggie_salad_bowl_count = chipo[chipo['item_name'] == 'Veggie Salad Bowl']['quantity'].sum()
print("Number of Veggie Salad Bowls ordered:", veggie_salad_bowl_count)

#Step 9. How many times did someone order more than one Canned Soda?
chipo_drink_steak_bowl = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
print(len(chipo_drink_steak_bowl))