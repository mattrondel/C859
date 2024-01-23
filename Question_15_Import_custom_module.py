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

import pigAge

input_pig_age = int(input())
# .strip() is optional with it looks like this:
# input_pig_age = int(input().strip())

converted_pig_age = pigAge.pigAge_converter(input_pig_age)

print(f"{input_pig_age} is {converted_pig_age} in human years")


stuff I put in the PA
import pigAge
input_pig_age = int(input())
# .strip() is optional with it looks like this:
# input_pig_age = int(input().strip())

converted_pig_age = pigAge.pigAge_converter(input_pig_age)
# you always need to address/call out a funtion from a module by ModuleName.ModuleFunction

# print statement reflects the original input
print(f"{input_pig_age} is {converted_pig_age} in human years")
# input_pig_age is converted_pig_age in human years
