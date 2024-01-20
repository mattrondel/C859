# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/14


# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a function and have it condensed and simplifed and break this down step by step so I can understand this

# Create a solution that accepts an integer input. Import the built-in module math and use its factorial() method to calculate the factorial of the integer input. Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100.
# The solution output should be in the format
# factorial_value
# Boolean_value
#  
# Sample Input/Output:
# If the input is
# 10
# then the expected output is
# 3628800
# True
# Alternatively, if the input is
# 3
# then the expected output is
# 6
# False

# *****
# 1. Accept an integer input.
# 2. Import the math module.
# 3. Calculate the factorial of the integer input using the factorial() method from the math module.
# 4. Output the factorial value.
# 5. Output a Boolean value indicating whether the factorial is greater than 100.

# Here is the simplified code without error checking, try/except, and functions:
# Step 1: Accept an integer input
n = int(input())

# Step 2: Import the math module
import math

# Step 3: Calculate the factorial of the input
factorial_value = math.factorial(n)

# Step 4: Output the factorial value
print(factorial_value)

# Step 5: Output a Boolean value indicating whether factorial > 100
print(factorial_value > 100)

# Now, let's understand each step:
 
# Step 1: n = int(input()) takes an integer input from the user and assigns it to the variable n.
 
# Step 2: import math imports the math module, which provides the factorial() method.
 
# Step 3: factorial_value = math.factorial(n) calculates the factorial of the input n using the factorial() method from the math module and assigns it to factorial_value.
 
# Step 4: print(factorial_value) outputs the calculated factorial value.
 
# Step 5: print(factorial_value > 100) outputs a Boolean value indicating whether the factorial is greater than 100. If it is, it prints True; otherwise, it prints False.
 
# You can use this code to input an integer, calculate its factorial, and check whether it's greater than 100.
