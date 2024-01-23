#this works for both PA and 
# PRO TIP: WHEN YOU COPY THE EQUALTION ITS IN SQUARE BRACKETS YOU NEED TO CHANGE THEM TO CURLY ONES
# tHIS PROBLEM BASICALLY GIVES YOU EVEYTHING YOU NEED FROM THE MATH EQUATION TO THE 3 INPUTS AND PRINT STATEMENT, ALL YOU HAVE TO DO IS PUT IT TOGETHER

#https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/4

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a function and have it condensed and simplifed and break this down step by step so I can understand this

# Task:
# Create a solution that accepts any three integer inputs representing the base (b1, b2) and height (h) measurements of a trapezoid in meters. 
#Output the exact area of the trapezoid in square meters as a float value. <-- how to do this? NOTE this does it automatically
# The exact area of a trapezoid can be calculated by finding the average of the two base measurements, then multiplying by the height measurement.
# Trapezoid Area Formula:
# A = [(b1 + b2) / 2] * h  <--- NOTE: IF you copy this it will use square brackets which is a list element and doesnt work
# The solution output should be in the format
# Trapezoid area: area_value square meters
#  
# Sample Input/Output:
# If the input is
# 3
# 4
# 5
# then the expected output is
# Trapezoid area: 17.5 square meters
# Alternatively, if the input is
# 3
# 5
# 7
# then the expected output is
# Trapezoid area: 28.0 square meters

# "take three inputs" 
b1 = int(input())
b2 = int(input())
h = int(input())

# "Trapezoid Area Formula:"
area_value = [(b1 + b2) / 2] * h

#again F strings to the rescue
print(f"Trapezoid area: {area_value} square meters")

