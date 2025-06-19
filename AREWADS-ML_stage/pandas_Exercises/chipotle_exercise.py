#Ex2 - Getting and Knowing your Data
#This time we are going to pull data directly from the internet. Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.

#Step 1. Import the necessary libraries
import pandas as pd
#Step 2. Import the dataset from this address.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
#Step 3. Assign it to a variable called chipo.
df = pd.read_csv(url, sep='\t')
chipo = df
#Step 4. See the first 10 entries
print(chipo.head(10))
#Step 5. What is the number of observations in the dataset?
# Solution 1
chipo.info()
# Solution 2
chipo.shape
#Step 6. What is the number of columns in the dataset?
chipo.shape
#Step 7. Print the name of all the columns.
chipo.columns
#Step 8. How is the dataset indexed?
chipo.index
#Step 9. Which was the most-ordered item?
most_ordered_item = chipo.groupby(['item_name']).agg({'quantity': 'sum'})
most_ordered_item.sort_values(by='quantity', ascending=False, inplace=True)
print(most_ordered_item.head(1))
#Step 10. For the most-ordered item, how many items were ordered?
most_ordered_quantity = most_ordered_item.iloc[0]['quantity']
print(f"The most ordered item was '{most_ordered_item.index[0]}' with a quantity of {most_ordered_quantity}.")
#Step 11. What was the most ordered item in the choice_description column?
most_ordered_choice = chipo.groupby(['choice_description']).agg({'quantity': 'sum'})
most_ordered_choice.sort_values(by='quantity', ascending=False, inplace=True)
print(most_ordered_choice.head(1))
#Step 12. How many items were orderd in total?
total_items_ordered = chipo['quantity'].sum()
print(f"Total items ordered: {total_items_ordered}")
#Step 13. Turn the item price into a float
#Step 13.a. Check the item price type
print(chipo.item_price.dtype)
#Step 13.b. Create a lambda function and change the type of item price
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer )
#Step 13.c. Check the item price type
print(chipo.item_price.dtype)
#Step 14. How much was the revenue for the period in the dataset?
revenue = (chipo['quantity'] * chipo['item_price']).sum()
print(f"Total revenue for the period: ${revenue:.2f}")
#Step 15. How many orders were made in the period?
orders_count = chipo['order_id'].nunique()
print(f"Total number of orders made: {orders_count}")
#Step 16. What is the average revenue amount per order?
# Solution 1
average_revenue_per_order = revenue / orders_count
print(f"Average revenue per order: ${average_revenue_per_order:.2f}")
# Solution 2
average_revenue_per_order = chipo.groupby('order_id').apply(lambda x: (x['quantity'] * x['item_price']).sum()).mean()
print(f"Average revenue per order: ${average_revenue_per_order:.2f}")
#Step 17. How many different items are sold?
different_items_sold = chipo['item_name'].nunique()
print(f"Total different items sold: {different_items_sold}")