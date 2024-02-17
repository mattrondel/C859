#  https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/5

#  Derek
#  * I got this wrong when I took the PA because I didn't follow the instructions on how to convert the inputs exactly. 
#  I did not initially convert the inputs to integer, instead I converted them when I computed the integer sum.
#  ==================================================
#  -A similar question appeared in my OA, but instead of outputting the sum of five inputs you only had to output the sum of three inputs.

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a function and have it condensed and simplifed and break this down step by step so I can understand this

#  
# Task:
# Create a solution that accepts five integer inputs. 
# Output the sum of the five inputs three times, converting the inputs to the requested data type prior to finding the sum.
  
# First output: sum of five inputs maintained as integer values
# Second output: sum of five inputs converted to float values
# Third output: sum of five inputs converted to string values (concatenate)
# The solution output should be in the format
# Integer: integer_sum_value Float: float_sum_value String: string_sum_value
#  
# Sample Input/Output:
# If the input is
# 1
# 3
# 6
# 2
# 7
# then the expected output is
# Integer: 19
# Float: 19.0
# String: 13627


# solution accepts five integer inputs
# solution outputs three sums of input values; convert before calculating sum
# first output: sum of five inputs maintained as integer values
# second output: sum of five inputs converted to float values
# third output: sum of five inputs converted to string values (concatenate)
# Accepting five integer inputs
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

# Calculating sums
integer_sum = num1 + num2 + num3 + num4 + num5
float_sum = float(integer_sum)
string_sum = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

# Outputting the results
print(f"Integer: {integer_sum}")
print(f"Float: {float_sum}")
print(f"String: {string_sum}")
