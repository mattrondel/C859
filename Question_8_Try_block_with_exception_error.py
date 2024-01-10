# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/8

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this with a try and except and not with a function and have it condensed and simplifed

# Create a solution that accepts one integer input representing the index value for any of the string elements in the following list:
# frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]
# Output the string element of the index value entered. The solution should be placed in a try block and implement an exception of "Error" if an incompatible integer input is provided.
# The solution output should be in the format
# frameworks_element
#  
# Sample Input/Output:
# If the integer input is:
# 2
# then the expected output is:
# CherryPy
# Alternatively, if the integer input is:
# 7
# then the expected output is:
# Error


# need to check this:

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

try:
    index = int(input())
    print(frameworks[index])
except (ValueError, IndexError):
    print("Error")
