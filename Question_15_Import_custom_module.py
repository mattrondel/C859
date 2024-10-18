# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/15
# Book material is Chapter 13 
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/13/section/1

# Try this lab:
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/15

# Me - trick to this is simply following what it asks and recalling that calling a funtion within a module is basically a file extention

# Derek
# I got this wrong when I took the PA because I forgot that when you use a function defined in an imported module 
# you have to preface the function with the name of the module.
# ==================================================
# -A similar question appeared in my OA, but instead of importing and using a module that calculates the human equivalent age of a pig you import and use a module that calculates the human equivalent age of a dog. 
# The solution and output were almost exactly the same.

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

import pigAge

input_pig_age = int(input())

converted_pig_age = pigAge.pigAge_converter(input_pig_age)

print(f"{input_pig_age} is {converted_pig_age} in human years")


# Stuff I put in the PA
import pigAge
input_pig_age = int(input())
# .strip() is optional with it looks like this:
# input_pig_age = int(input().strip())

converted_pig_age = pigAge.pigAge_converter(input_pig_age)
# you always need to address/call out a funtion from a module by ModuleName.ModuleFunction

# print statement reflects the original input
print(f"{input_pig_age} is {converted_pig_age} in human years")
# input_pig_age is converted_pig_age in human years
