# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/11

# consider:
# https://aiplanet.com/learn/5-week_Data_Science_Bootcamp/week-0/150/conditional-statement-and-dictionaries

# The thing at the bottom is called conditional expression also known as ternary operators
# zybooks lesson on it
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/5/section/12

# zybooks on Dictonaries
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/11/section/12

# Derek notes
# -A similar question appeared in my OA, but instead of computing the total purchase cost of an input number of a specified grocery store item and calculating a discount, 
# you had to compute the total cost of tuition for an input number of course credits for a specified school and calculate a discount. 
# The solution and output were almost exactly the same.

# Create a solution that accepts a string input representing a grocery store item and an integer input identifying the number of items purchased on a recent visit. 
# The following dictionary purchase lists available items as the key with the cost per item as the value.
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

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

# NEED A BREAK DOWN OF THIS AS THE QUESTION PRESENTS ITSELF JUST AS I DID FOR THE FIRST FEW QUESTIONS

# Sample Input
# "Create a solution that accepts a string input representing a grocery store item and an 
# integer input identifying the number of items purchased on a recent visit. "

Other way to solve it:

item = input()
quantity = int(input())

base_price = purchase[item] * quantity
discount = 0

if quantity >= 21:
    discount = 0.10
elif quantity >= 10:
    discount = 0.05

total = base_price * (1 - discount)

print(f"{item} ${total:.2f}")

######################################################
Longer way to solve it:


item_input = input()
quantity_input = int(input())

# Calculate total cost without discount
# The 0 in .get(item_input, 0) is there for error checking and is optional
# total_cost = purchase.get(item_input, 0) * quantity_input
total_cost = purchase.get(item_input) * quantity_input

# Determine discount based on quantity
# If fewer than ten items are purchased, the price is the full cost per item.
# If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount.
# If twenty-one or more items are purchased, the purchase gets a 10% discount.
discount = 0 if quantity_input < 10 else 0.05 if 10 <= quantity_input <= 20 else 0.10

# Calculate discounted cost
discounted_cost = total_cost * (1 - discount)

# Format and print the result
# Output the chosen item and total cost of the purchase to two decimal places.
# The solution output should be in the format
# item_purchased $total_purchase_cost
result = f"{item_input} ${discounted_cost:.2f}"
print(result)
