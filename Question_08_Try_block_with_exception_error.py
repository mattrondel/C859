# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/8

# FreeCodeCamp Video: (3:04:17) Try / Except
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=11057s

# WGU Chapter 11 (Exceptions) (30 min)
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ceab3ff7-8098-4cd5-b976-add60029f03e

# lesson that goes with it
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/12/section/9

# Automate the boring stuff
# https://automatetheboringstuff.com/2e/chapter8/

# book material on this
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/12/section/1

# Read more here https://docs.python.org/3/library/exceptions.html

# FREE CODE CAMP:
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=4173s

# Derek
# -A similar question appeared in my OA, but instead of outputting the string element of the input index value you had to output the index based on the input string value. 
# The solution and output were almost exactly the same. Instead of using frameworks[user_input] use frameworks.index(user_input)
----------------------------------------
# What Derek is talking about might look like this:

# frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

# try:
#     search_string = int(input())
#     index = frameworks.index(search_string)
            #Note: The index() method in Python is a built-in method for lists. It is used to find the index of the first occurrence of a specified element in the list.
#     print(index)
# except ValueError:
#     print("Error")

# In this code:

# - Instead of converting the input directly into an integer (index = int(input())), we directly take the input as a string (search_string = input()).
# - We use the index() method of lists to find the index of the input string value within the frameworks list.
# - If the input string is not found in the list, a ValueError will be raised. We catch this ValueError to handle the case where the 
# input string is not found in the list and print an error message accordingly.
----------------------------------------

# Need this one explained mainly the ValueError and IndexError - see below @ "BREAKING THIS DOWN (again)"

# that and why does the except (ValueError, IndexError): not contain a colon after the except - this is because the code isn't written this way

# Create a solution that accepts one integer input representing the index value for any of the string elements in the following list:
# frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]
# Output the string element of the index value entered. 
# The solution should be placed in a try block and implement an exception of "Error" if an incompatible integer input is provided.

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

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

try:
    index = int(input())
    print(frameworks[index])
except (ValueError, IndexError):
    print("Error")

# AS READ IN THE QUESTION - this is tricky as what derek says this might be drastiucally different 
# Derek said: output the index based on the input string value

# "Create a solution that accepts one integer input representing the index value"
index = int(input())
# The solution should be placed in a try block and implement an exception of "Error" if an incompatible integer input is provided.
# try:
#     index = int(input())
#     print(frameworks[index])
# except (ValueError, IndexError):
#     print("Error")


# BREAKING THIS DOWN (again)
# This is the provided text just make sure its present
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

# This is begining of the try block it starts the program as normal but has error checking enabled 
# and the code becomes indented, if it fails then it gets "bumped" to the except block section when it sees the errors stated in the 
try:
# The try block begins. Inside this block, the program tries to execute the following steps:
    index = int(input())
# a. It prompts the user to input an integer value. This integer represents the index of the framework they want to access from the list.
# b. It attempts to convert the user input to an integer using the int() function.
    print(frameworks[index])
# c. It then tries to print the framework name located at the index provided by the user within the frameworks list.
except (ValueError, IndexError):
# If any exceptions occur during these steps, the except block is triggered. This block catches two types of exceptions:
# a. ValueError: This occurs if the user input cannot be converted to an integer. For example, if the user enters a non-numeric value like "abc".
# b. IndexError: This occurs if the index provided by the user is out of range for the frameworks list. For example, if the user enters an index that is too large or negative.
    print("Error")
# If either a ValueError or IndexError occurs, the program prints "Error".

# Exception types explained
# ValueError - if the user provides input that cannot be converted to an integer, it would be appropriate to raise this exception type
# IndexError - This exception occurs when you're trying to access an index in a list that doesn't exist

#############
# In the provided Python code, ValueError and IndexError are used to handle potential exceptions that might occur during the execution of the code within the try block.

# Let's break down the code:

# 1. index = int(input()): This line takes user input and converts it to an integer. 
# If the user enters something that cannot be converted to an integer (e.g., a string or a floating-point number), a ValueError will be raised.

# 2. print(frameworks[index]): This line tries to access an element at the specified index in the frameworks list. 
# If the index is out of bounds (i.e., it is greater than or equal to the length of the list), an IndexError will be raised.

# 3. except (ValueError, IndexError):: This block catches any ValueError or IndexError that might occur in the preceding try block. 
# If either of these exceptions is raised, the code inside the except block will be executed.

# 4. print("Error"): This line prints the message "Error" to the console if a ValueError or IndexError occurs.

# In summary, the ValueError is used to handle cases where the user enters input that cannot be converted to an integer, and the IndexError
# is used to handle cases where the index used to access the frameworks list is out of bounds. 
# The except block is responsible for handling these specific types of exceptions and printing an error message.

Breaking down what its asking:
"Create a solution that accepts one integer input representing the index value "
index = int(input())
"Output the string element of the index value entered."
"Output" means print() and "string element" is fancy word for variable name of sample provided
print(frameworks[index])
becuase frameworks is a list you have to address the print statement in the same fashion as the provided code

"exception of "Error" if an incompatible integer input is provided."
this means you need a print("Error")

build out the structure then add the try and except lines
try: statements always seem to be setup as :
try:
    problem here
excepts are different as they can be like:
except:
    or
except ValueError:
ValueError might be speciifed or worst case you have to know they error its asking for
Multiple exception types in a single exception handler may look like this:
except (NameError, AttributeError):
they are always contained in a () with commas to seprate then the colon:
basically its "if you encounter these specific errors then do this next thing otherwise skip down"
