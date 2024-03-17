# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/7
#  Explain line 21 of result = input_value > max(predef_list) and how to interprite the question to a python solution

# Derek
# A similar question appeared in my OA, but instead of determining if the input integer was greater than the maximum value in the 
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

# This is the provided List:
predef_list = [4, -27, 15, 33, -10]

# "Create a solution that accepts an integer input" so send that integer input to some variable
input_value = int(input())

# This is the meat and poatatoes of the problem:
# "maximum value from predef_list" this is refering to max() built-in function
# the max() function is a built-in function used to find the maximum element from a collection in this case its the predef_list as requested
# This statement is basically saying take the input value from the begining of the script and is it > (or >= depending on the question) the maximum element aka number found in the predef_list supplied
Boolean_value = input_value > max(predef_list)

# The solution output should be in the format: Greater Than Max? Boolean_value" 
# Just copy paste and turn it into f strings take that provded varable and use it in the meat and potatoes

print(f"Greater Than Max? {Boolean_value}")

DONT FORGET TO BUILD YOUR F STRINGS CORRECLY!! F"WORDS {VARABLES}")
