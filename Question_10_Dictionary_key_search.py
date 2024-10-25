# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/10


THIS IS A THREE PART PROBLEM
input, solve (using the sample data), then output

# might be the same here:
# https://brainly.com/question/39010072

# FreeCodeCamp Video: (2:07:17) Dictionaries
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=7637s

# Corey Schafer videos: Corey Schafer: Dictionaries + Key-Value Pairs
# https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5

# Socratica You Tube Videos: Socratica: Python Dictionaries
# https://www.youtube.com/watch?v=XCcpzWs-CI4

# WGU  - Strings, Lists, and Dictionaries
# Chapter 11 (Lists and Dictionaries) (24 min)
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=905f48cc-26b5-4ed1-b79e-add6010a9bde

# dictionaryies go as follows:
# Dictonaryname = {key:value}
# muliple dictonary items are seprated with commas
# Dictonaryname.get(key) fetches the key

# Further learning on dicotonaries https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

# Derek
# -A similar question appeared in my OA, but instead of computing the total cost of stocks selected you had to compute the total cost of snacks selected from a vending machine. 
# The solution and output were almost exactly the same.

# NEED DETAILED EXPLAINING ON THIS ONE

# Create a solution that accepts an integer input identifying how many shares of stock are to be purchased from the Old Town Stock Exchange, followed by an equivalent 
# number of string inputs representing the stock selections. The following dictionary stock lists available stock selections as the key with the cost per selection as the value.
# 
# stocks = {'TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}
#
# Output the total cost of the purchased shares of stock to two decimal places.
# The solution output should be in the format
#
# Total price: $cost_of_stocks
#  
# Sample Input/Output:
# If the input is
# 3
# SOFI
# AMZN
# LVLU
# then the expected output is
# Total price: $150.53

# provided line:
stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

num_shares = int(input())
total_price = sum(stocks.get(input(), 0) for _ in range(num_shares))

print(f"Total price: ${total_price:.2f}")


# two decimal places keyword for :.2f
# THINK OF THE .2 AS IN .2 DECINAL PLACES AND THE f IS FOR FORMAT, the F stands for float and the .2 is how many decimal places will show

# with .strip() is optional would look like this:
# total_price = sum(stocks[input().strip()] for _ in range(int(input())))


############################### 
######## Snack Machine ######## 
############################### 

Final answer:

To calculate the total cost of snacks from a vending machine, you can write a program that takes the quantity and types of items as input, 
then uses a dictionary of snack prices to compute and print the total cost.

Explanation:

To tackle this task, you could create a Python program (for example) that would request an integer input for the quantity of items and then 
request an equivalent number of string inputs for the snack selection. Using the provided dictionary of snack selections and their respective 
prices, your code would calculate the total price of the snacks by adding together the prices of the inputted selections.

Here's a simplified example of what that code could look like:

snacks = {'A1': 0.25, 'A2': 0.50, 'A3': 0.75, 'B1': 1.50, 'B2': 1.75, 'B3': 2.00, 'C1': 0.25, 'C2': 0.45, 'C3': 0.30}

total_snacks = int(input('Enter the total number of snacks: '))
total_cost = 0
for _ in range(total_snacks):
 selection = input('Enter a snack selection: ')
 total_cost += snacks[selection]
print(f'Total price: ${total_cost:.2f}')

This program first takes an integer input total_snacks, then for each snack requested, it adds to the total_cost using the snack's corresponding 
price in the snack dictionary. Finally, it prints the total cost with a dollar sign and two decimal points of precision.


