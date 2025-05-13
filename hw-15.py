'''
Author:     Cody Costa
Date:       5/13/2025

'''

# generate random set of fruit vendor inventory
import random

fruits = ['Apple', 'Banana', 'Blueberry', 'Grape', 'Mango', 'Strawberry', 'Plum', 'Blackberry', 'Orange', 'Raspberry']
prices = [random.randint(1, 5) for _ in range(10)]
quantities = [random.randint(1, 25) for _ in range(10)]

my_inventory = {}

for index, fruit in enumerate(fruits):
    my_inventory[fruit] = (prices[index], quantities[index])

print(f'Inventory: {my_inventory}')


# calculate total value of inventory goods
total_value = 0
for key in my_inventory.keys():
    # price = dict[key][0]
    # quant = dict[key][1]
    total_value += (my_inventory[key][0] * my_inventory[key][1])

print(f'Inventory value = ${total_value}\n')


# loop again but selling goods this time
sales = {}
for idx, key in enumerate(my_inventory.keys()):
    if idx == 0:
        # inital fruit inventory
        previous_fruit_inventory = my_inventory[key][1]
        continue

    current_fruit_inventory = my_inventory[key][1]
    current_fruit_price = my_inventory[key][0]

    if current_fruit_inventory > previous_fruit_inventory:
        sales[key] = (previous_fruit_inventory, previous_fruit_inventory * current_fruit_price)

    previous_fruit_inventory = current_fruit_inventory

print(f'Sales Log: {sales}\n')


# calculate total sales
total_sales = 0
for key in sales.keys():
    num_sold = sales[key][0]
    profit = sales[key][1]

    print(f'Sold {num_sold} {key} for total profit of ${profit}')
    total_sales += profit

print(f'\nTotal Sales = ${total_sales}')