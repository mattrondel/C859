# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/14


# WGU help function 
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=43b25501-be6b-4b36-868b-a89b01034524

# Try this lab:
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/14

# https://learn.zybooks.com/zybook/WGUC859v4/chapter/22/section/8

#info on built-in function in python https://www.geeksforgeeks.org/factorial-in-python/

# Derek
# "-A similar question appeared in my OA, but instead of importing the math module, using the factorial() method on an integer input, and then determining if the result was greater than 100, 
# you had to use the sqrt() method on an integer input and determine if the result was a perfect square. 
# The solution and output were almost exactly the same."


solution to zybooks

import math

number = int(input())

factorial_value = math.factorial(number)
Boolean_value = factorial_value > 100

print(factorial_value)
print(Boolean_value)


#####################################################################
# if Derek is correct then it might look like this:
probably should get coles help on this

# Need to test the below in the blank zybook lab:
https://learn.zybooks.com/zybook/WGUC859v4/chapter/2/section/16
"python use the sqrt() method on an integer input and determine if it is a perfect square"


# This worked for perfect square but does not use the sqrt() method 
num = int(input()) 
sqrt_num = num ** 0.5  
if sqrt_num.is_integer():
    print("The provided number is a perfect square")  
else:
    print("The provided number is not a perfect square")  

# This works too
import math  
num = int(input())
sqrt_num = math.sqrt(num)  
if sqrt_num.is_integer():  
    print("The number is a perfect square")  
else:  
    print("The number is not a perfect square")

To create a solution that accepts an integer input, calculates the 
square root using the sqrt() method from the math module, and 
determines whether the output is a perfect square, you can follow these steps:

1. Begin by importing the math module at the beginning of your code with 
the following line: `import math`

2. Prompt the user to enter an integer by using an input() function. Assign
the input to a variable, let's say `num`.

3. Convert the input from a string to an integer using the int() function, like
this: `num = int(num)`

4. Calculate the square root of the input using the sqrt() method from the 
math module. Assign the result to a variable, let's say `sqrt_value`. The
code for this step will be: `sqrt_value = math.sqrt(num)`

5. Check if the square root value is an integer by comparing it with its
rounded value. If the rounded value is equal to the square root value, it
means the number is a perfect square. In this case, assign the Boolean value
True to a variable, let's say `is_perfect_square`. Otherwise, assign 
False. The code for this step will be:

```
rounded_value = round(sqrt_value)
is_perfect_square = rounded_value == sqrt_value
```

6. Finally, output the square root value and the Boolean value identifying
whether it is a perfect square or not. You can use the print() function 
for this step, like this:

```
print("Square root:", sqrt_value)
print("Is a perfect square:", is_perfect_square)
```

To summarize, the solution will involve importing the math module, 
accepting an integer input from the user, calculating the square root using
sqrt(), determining whether the output is a perfect square, and then
printing the square root value and the Boolean value indicating whether it
is a perfect square or not.

#####################################################################


import math
# Define an integer input
number = int(input())
# Calculate the factorial
factorial_result = math.factorial(number)
# Print the result
print("The factorial of", number, "is:", factorial_result)

# ------------

# More accurately with the full details he provided it might look closer to this:
import math

number = int(input())
factorial_result = math.factorial(number)
square_root = math.sqrt(factorial_result)

if square_root.is_integer():
    print("Factorial of", number, "is greater than 100 and its square root is a perfect square:", int(square_root))

# using f strings instead

import math
number = int(input())
factorial_result = math.factorial(number)
square_root = math.sqrt(factorial_result)

if square_root.is_integer():
    print(f"Factorial of {number} is greater than 100 and its square root is a perfect square: {int(square_root)}")

import math

# Accept user input for the number
number = int(input())

# Calculate the factorial
factorial_result = math.factorial(number)

# Calculate the square root
square_root = math.sqrt(factorial_result)

# Check if the square root is a perfect square
if square_root.is_integer():
    print(f"Factorial of {number} is greater than 100 and its square root is a perfect square: {int(square_root)}")


# ------------
BREAKDOWN AS THE QUESTION PRESENTS ITELF

# "Create a solution that accepts an integer input"
number = int(input())
#  "Import the built-in module math"
import math
# "...use its factorial() method to calculate the factorial of the integer input. "
factorial_value = math.factorial(n)
# "Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100."
# "The solution output should be in the format"
# "factorial_value"
# "Boolean_value"

print(factorial_value)
print(factorial_value > 100)




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
