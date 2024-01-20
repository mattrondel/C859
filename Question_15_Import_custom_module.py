# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/15

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, 
#do this without a try and except and not with a function and have it condensed and simplifed and break this down step by step so I can understand this

# Create a solution that accepts an integer input representing the age of a pig. 
# Import the existing module pigAge and use its pre-built pigAge_converter() function to calculate the human equivalent age of a pig. 
# A year in a pig's life is equivalent to five years in a human's life. Output the human-equivalent age of the pig.
# The solution output should be in the format
# input_pig_age is converted_pig_age in human years
#  
# Sample Input/Output:
# If the input is
# 8
# then the expected output is
# 8 is 40 in human years

# Import the pigAge module
import pigAge

# Accept an integer input representing the age of a pig
input_pig_age = int(input("Enter the age of the pig: "))

# Use the pigAge_converter() function to calculate the human equivalent age of the pig
converted_pig_age = pigAge.pigAge_converter(input_pig_age)

# Calculate the human equivalent age (5 years in human's life for 1 year in pig's life)
converted_pig_age *= 5

# Output the result in the specified format
print(f"{input_pig_age} is {converted_pig_age} in human years")

# This code prompts the user to enter the age of the pig, calculates the human equivalent age using the pigAge_converter function, 
# multiplies it by 5 (since 1 year in a pig's life is equivalent to 5 years in a human's life), and then prints the result in the specified format.

# ********************************
# Broken Down Step by Step
# ********************************

# 1. Import the pigAge module:
import pigAge

# This line imports the pigAge module, which contains a pre-built function called pigAge_converter that we'll use to calculate the human equivalent age of a pig.

#2.  Accept an integer input representing the age of a pig:
input_pig_age = int(input("Enter the age of the pig: "))

# 3. Use the pigAge_converter() function:
converted_pig_age = pigAge.pigAge_converter(input_pig_age)

# This line calls the pigAge_converter function from the imported pigAge module, passing the entered pig age as an argument. 
# The result is stored in the variable converted_pig_age.

# 4. Calculate the human equivalent age:
converted_pig_age *= 5

# Since a year in a pig's life is equivalent to five years in a human's life, we multiply the converted_pig_age by 5 to get the human equivalent age.

# 5. Output the result in the specified format:
print(f"{input_pig_age} is {converted_pig_age} in human years")

# This line prints the final result in the specified format, using an f-string to include the entered pig age (input_pig_age) and the calculated human equivalent age (converted_pig_age).

# So, in summary, the code imports the necessary module, takes user input, performs the conversion using the provided function, adjusts for the conversion ratio, and then prints the result.
