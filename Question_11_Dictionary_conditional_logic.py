# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/11

Blank Zybooks lab 2.16 

https://learn.zybooks.com/zybook/WGUC859v4/chapter/2/section/16

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

if quantity >= 21:
    discount = 0.10
elif quantity >= 10:
    discount = 0.05
else:
    discount = 0

total = base_price * (1 - discount)

print(f"{item} ${total:.2f}")

THIS ABOVE EXPLAINED:

Given input items DONT MISPELL THE WORD INPUT!!!

item = input()
quantity = int(input())

you will need to have a base price in order to determine costs 

purchase[item] the word "purchase" is the name of the dictonary list and the [] is input variable this grabs the key which in this case is a price , the [input] "grabs" the other number

base_price = purchase[item] * quantity


If twenty-one or more items are purchased, the purchase gets a 10% discount. 10% in decimal is 0.10
elif quantity >= 10 
If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount. greater than or = to 10
this is a bit tricky to figure out 

if quantity >= 21:
    discount = 0.10
elif quantity >= 10:
    discount = 0.05
else:
    discount = 0


The (1 - discount) part:
When calculating a discounted price, you need to subtract the discount from 1 (100% aka 1.00) to get the actual percentage you pay. 
this is a way flips the number like 0.10 - 1.00 gives us 0.90 which then * times the base price

total = base_price * (1 - discount)

print statement with f strings adjustments

print(f"{item} ${total:.2f}")

for :.2f think of .2f as an extension or read it like colon .2f, the colon serves as append the .2f file extension



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
