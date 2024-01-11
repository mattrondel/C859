# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/11

# Create a solution that accepts a string input representing a grocery store item and an integer input identifying the number of items purchased on a recent visit. The following dictionary purchase lists available items as the key with the cost per item as the value.
# purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}
# Additionally,
#  
# If fewer than ten items are purchased, the price is the full cost per item.
# If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount.
# If twenty-one or more items are purchased, the purchase gets a 10% discount.
# Output the chosen item and total cost of the purchase to two decimal places.
# The solution output should be in the format
# item_purchased $total_purchase_cost
#  
# Sample Input/Output:
# If the input is
# bananas
# 12
# then the expected output is
# bananas $21.09
# Alternatively, if the input is
# cookies
# 144
# then the expected output is
# cookies $585.79

# Sample Input
item_input = input()
quantity_input = int(input())

# Calculate total cost without discount
total_cost = purchase.get(item_input, 0) * quantity_input

# Determine discount based on quantity
discount = 0 if quantity_input < 10 else 0.05 if 10 <= quantity_input <= 20 else 0.10

# Calculate discounted cost
discounted_cost = total_cost * (1 - discount)

# Format and print the result
result = f"{item_input} ${discounted_cost:.2f}"
print(result)
