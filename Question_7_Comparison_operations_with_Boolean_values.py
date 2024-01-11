# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/7
# 
# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a function and have it condensed and simplifed and break this down step by step so I can understand this
#
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
