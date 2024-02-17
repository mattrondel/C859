# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/3

# need this part explained and why the [index] is nested
# {type(various_data_types[index])

# Derek:
# * I got this wrong when I took the PA because I didn't know how to get the name of the data type by using the .name attribute. 
# I didn't read all of the details provided with the question, and a hint on how to use it was right there.
# -A similar question appeared in my OA, but instead of needing to use the .__name__ attribute to output the data type, you only had to output the data type using the default output of the type() function. 
# The solution and output were almost exactly the same.

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a function and have it condensed and simplifed and break this down step by step so I can understand this

# Instructions:
# Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.
#  
# Task:
# Create a solution that accepts an integer input representing the index value for any any of the five elements in the following list:
# various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]
# Using the built-in function type() and getting its name by using the .name attribute, output data type (e.g., int”, “float”, “bool”, “str”) based on the input index value of the list element.
# The solution output should be in the format
# Element index_value: data_type
#  
# Sample Input/Output:
# If the input is
# 4
# then the expected output is
# Element 4: tuple

index = int(input())
various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]
print(f"Element {index}: {type(various_data_types[index]).__name__}")

#".name attribute" is called this but means dunder .name or .__name__

# The .__name__ attribute is used to obtain the name of a class or type in Python. When applied to the result of the type() function, it returns the name of the data type as a string.

# In the provided solution, type(various_data_types[index]).__name__ is used to extract the name of the data type of the element at the specified index in the list various_data_types.

# Here's the explanation of each part:

# type(various_data_types[index]): This part gets the type (class) of the element at the specified index in the list.

# .__name__: This part accesses the __name__ attribute of the type, which holds the name of the type as a string.

# So, in short, .__name__ is used to obtain a human-readable name for the type.

# If you want to avoid using .__name__, you could directly print the result of type() without the attribute. However, using .__name__ provides a cleaner and more readable output in this context. Here's an alternative without .__name__:
