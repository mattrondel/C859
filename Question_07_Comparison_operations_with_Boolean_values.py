# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/7
#  Explain line 21 of result = input_value > max(predef_list) and how to interprite the question to a python solution

# Derek
# -A similar question appeared in my OA, but instead of determining if the input integer was greater than the maximum value in the 
# list you had to determine if the input integer was greater than or equal to the maximum value in the list. 
# The solution and output were almost exactly the same.

# Task:
# Create a solution that accepts an integer input to compare against the following list:
# predef_list = [4, -27, 15, 33, -10]
# Output a Boolean value indicating whether the input value is greater than the maximum value from predef_list
# The solution output should be in the format
# Greater Than Max? Boolean_value
#  
# Sample Input/Output:
# If the input is
# 20
# then the expected output is
# Greater Than Max? False

predef_list = [4, -27, 15, 33, -10]
input_value = int(input())
result = input_value > max(predef_list)
print(f"Greater Than Max? {result}")

# This code takes an integer input, compares it with the maximum value from the predef_list, and prints the result in the specified format.
