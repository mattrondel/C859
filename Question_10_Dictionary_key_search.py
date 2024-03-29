# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/10

FreeCodeCamp Video: (2:07:17) Dictionaries
https://www.youtube.com/watch?v=rfscVS0vtbw&t=7637s

Corey Schafer videos: Corey Schafer: Dictionaries + Key-Value Pairs
https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5

Socratica You Tube Videos: Socratica: Python Dictionaries
https://www.youtube.com/watch?v=XCcpzWs-CI4

WGU  - Strings, Lists, and Dictionaries
Chapter 11 (Lists and Dictionaries) (24 min)
https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=905f48cc-26b5-4ed1-b79e-add6010a9bde


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
total_price = sum(stocks.get(input().strip(), 0) for _ in range(num_shares))

print(f"Total price: ${total_price:.2f}")


# two decimal places keyword for :.2f
# THINK OF THE .2 AS IN .2 DECINAL PLACES AND THE f IS FOR FORMAT, thje F stands for float and the .2 is how many decimal places will show

# with .strip() is optional would look like this:
# total_price = sum(stocks[input().strip()] for _ in range(int(input())))


