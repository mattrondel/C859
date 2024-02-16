# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/14

# Try this lab:
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/14

# "-A similar question appeared in my OA, but instead of importing the math module, using the factorial() method on an integer input, and then determining if the result was greater than 100, you had to use the sqrt() method on an integer input and determine if the result was a perfect square. 
# The solution and output were almost exactly the same."

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

########### Easier to Read ###########
import math
n = int(input())
factorial_value = math.factorial(n)
print(factorial_value)
print(factorial_value > 100)

# Now, let's understand each step as stated by the questions
#Create a solution that accepts an integer input - in my case I'm sending it to variable n
n = int(input())

# Import the built-in module math but make sure it goes to the top of the script
import math

# as stated "Use its factorial() method to calculate the factorial of the integer input." 
# Literarly copy factorial() and put our variable in the bracets but you have to call the funtion with the module name because its the rules baby!
#factorial() -> math.factorial() with our variable in the braces
# math.factorial(n)
# then send this to a variable like so:
# output = math.factorial(n)
# it says "value of the factorial" so lets change this to factorial value like so:
factorial_value = math.factorial(n)

#Now the print statements:
# They are asking for statements on two lines like so:
# "Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100." so two print statements

print(factorial_value)
print(factorial_value > 100)



######################## Older notes ########################
# Step 1: n = int(input()) takes an integer input from the user and assigns it to the variable n.
# Step 2: import math imports the math module, which provides the factorial() method.
# Step 3: factorial_value = math.factorial(n) calculates the factorial of the input n using the factorial() method from the math module and assigns it to factorial_value.
# Step 4: print(factorial_value) outputs the calculated factorial value.
# Step 5: print(factorial_value > 100) outputs a Boolean value indicating whether the factorial is greater than 100. If it is, it prints True; otherwise, it prints False.
# You can use this code to input an integer, calculate its factorial, and check whether it's greater than 100.
