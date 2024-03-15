# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/3

# need this part explained and why the [index] is nested
# {type(various_data_types[index])

# book material on this:
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/4/section/1

# Derek:
# * I got this wrong when I took the PA because I didn't know how to get the name of the data type by using the .name attribute. 
# I didn't read all of the details provided with the question, and a hint on how to use it was right there.
# -A similar question appeared in my OA, but instead of needing to use the .__name__ attribute to output the data type, you only had to 
# output the data type using the default output of the type() function. 
# The solution and output were almost exactly the same.

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

# Step one is taking the "what kind of input are we wanting"
index = int(input())

# Step 2 is copying the provided stuff they give you
various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

# step 3 is outputing and modifying as requested, in this case its a two-part print statement -one being the index number from input and the other "the tricky part of this problem"
print(f"Element {index}: {type(various_data_types[index]).__name__}")
# the .__name__ will output the name of the type like "int" or "bool" if you do not add the .__name__ you get  "<class 'int'>" or "<class 'bool'>"
#".name attribute" is called this but means dunder .name or .__name__
# The .__name__ attribute is used to obtain the name of a class or type in Python. 
# When applied to the result of the type() function, it returns the name of the data type as a string.
# In the provided solution, type(various_data_types[index]).__name__ is used to extract the name of the data type of the element at the specified index in the list various_data_types.
# Here's the explanation of each part:
# type(various_data_types[index]): This part gets the type (class) of the element at the specified index in the list, the index is the orginal input value at the begining of the script.
# .__name__: This part accesses the __name__ attribute of the type, which holds the name of the type as a string.
# So, in short, .__name__ is used to obtain a human-readable name for the type.
# If you want to avoid using .__name__, you could directly print the result of type() without the attribute. However, using .__name__ provides a cleaner and more readable output in this context. 

#Tips on building this out 3/4/24:
index = int(input())
various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

# print(f"Element {index}: {type(various_data_types[index]).__name__}")

# Start by builing out the print statement as its stated in the example (copy/paste then edit for f strings
# print(f"Element {index}: {data_type}")
# Note that it says data_type but don't take this too literal just go by type() above, we are just using the suggested varable in the example

# Use the built-in funtion type() as requested but since we're working with f strings we use {} instead of () on the outside so do it like so:
# Basically we nest the suggested varable inside type()
# print(f"Element {index}: {type(various_data_types)}")

# Now add in the various_data_types variable becuase thats what we need type() run against
# print(f"Element {index}: {type(various_data_types)}")

# Now add [index] next to various data types so it can retrieve the element from the list 
# Note that this is the same index variable used in the begining and since its a list it uses the square brackets []. 
# It should now look like this:
# print(f"Element {index}: {type(various_data_types[index])}")

# Now like a file extension in order to get the name of the type add .__name__ (Thats dot dunder name dunder) to the tail end of type() 
# This is how we run it against the built-in type() funtion
# like so:
print(f"Element {index}: {type(various_data_types[index]).__name__}")
# then Blammo! you're done
