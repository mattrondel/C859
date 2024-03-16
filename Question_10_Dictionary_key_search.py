# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/10

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


print(f'Total price: ${total_price:.2f}')
total_price = sum(stocks[input()] for _ in range(int(input())))

# two decimal places keyword for :.2f
# THINK OF THE .2 AS IN .2 DECINAL PLACES AND THE f IS FOR FORMAT, thje F stands for float and the .2 is how many decimal places will show

# with .strip() is optional would look like this:
# total_price = sum(stocks[input().strip()] for _ in range(int(input())))


