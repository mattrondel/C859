# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/13

# Book content
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/14/section/7

# Coreys video: https://www.youtube.com/watch?v=q5uM4VKywbA

# practice here:
# https://replit.com/@mrondel/Mailpy#main.py
# or here :
# https://replit.com/@mrondel/mainpy-1#main.py

#######################################################
# Is this similar to Question 12 but the csv module? Need help solving
#######################################################

# Derek
# * I got this wrong when I took the PA because I forgot the syntax for using the CSV reader method.
# ==================================================
# -A similar question appeared in my OA, but instead of reading the CSV file content and creating a dictionary you had to create a list. 
# The solution is mostly similar and the output was almost exactly the same. 
# Once you have the CSV file open and ready to read the rows of content, instead of creating dictionary KEY and VALUE pairs and adding 
# them to a dictionary, just use the list.append() method to add each row to a list.


# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a function and have it condensed and simplifed and break this down step by step so I can understand this

# Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". Each file contains two rows of comma-separated values. 
# Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values 
# in the specified file. Output the file contents as two dictionaries.
# The solution output should be in the format
# {key:value,key:value,key:value}
# {key:value,key:value,key:value}
#  
# Sample Input/Output:
# If the file content is
# input1.csv
# then the expected output is
# {a:100,b:200,c:300}
# {bananas:1.85,steak:19.99,cookies:4.52}
# Alternatively, if the file content is
# input2.csv
# then the expected output is
# {d:400,e:500,f:600}
# {celery:2.81,milk:4.34,bread:5.63}

# sample file:
# input1.csv
# contents:
#  a, 100, b, 200, c, 300
# bananas, 1.85, steak, 19.99, cookies, 4.52

# This works:

import csv

file_name = input()

with open(file_name, 'r') as file:
    csv_reader = csv.reader(file)
    dict1, dict2 = ({row[i].strip(): row[i + 1].strip() for i in range(0, len(row), 2)} for row in [next(csv_reader), next(csv_reader)])
    # Me trying to break this down to read it easier (this is a copy of the above):
    #dict1, dict2 = ({row[i]: row[i + 1] for i in range(0, len(row), 2)}for row in [next(csv_reader), next(csv_reader)])

print(dict1)
print(dict2)

#########################################
# Explained:
#########################################

# 1. Import the csv module:

import csv

# This line imports the csv module, which provides functionality for reading and writing CSV files.

# 2. Accept the CSV file name as input:

file_name = input()

# This line prompts the user to enter the name of the CSV file, and the input is stored in the variable file_name

# Step 3 Open the CSV file for reading:

with open(file_name, 'r') as file:

# This line uses a with statement to open the specified CSV file (file_name) in read mode ('r'). The with statement ensures that the file is properly closed after reading.

# 4. Create a CSV reader:

csv_reader = csv.reader(file)

# This line creates a CSV reader object (csv_reader) using the opened file. The reader object is used to iterate through the rows of the CSV file.

# 5. Read two rows of comma-separated values:
# The next() function returns the next item in an iterator. An iterable is anything that you can loop over.
row1 = next(csv_reader)
row2 = next(csv_reader)

# These lines use the next() function to retrieve the next two rows from the CSV file. Each row is a list of comma-separated values.

# 6. Create dictionaries for the two rows:

dict1 = {row[i].strip(): row[i + 1].strip() for i in range(0, len(row), 2)} for row in [row1]
dict2 = {row[i].strip(): row[i + 1].strip() for i in range(0, len(row), 2)} for row in [row2]

# These lines use dictionary comprehensions to create dictionaries for each row. The strip() method is applied to remove leading and trailing whitespaces from the keys and values.

7. Print the dictionaries:

print(dict1)
print(dict2)

# These lines print the resulting dictionaries to the console.
#########

# Step 6 broken down:
# Step 6 Is where dictionaries are created for the two rows of comma-separated values.

dict1 = {row[i].strip(): row[i + 1].strip() for i in range(0, len(row), 2)} for row in [row1]
dict2 = {row[i].strip(): row[i + 1].strip() for i in range(0, len(row), 2)} for row in [row2]

# Here, row1 and row2 are the two rows of comma-separated values obtained from the CSV file. For the sake of explanation, let's focus on dict1:

# 1. {...} for row in [row1]: This is a dictionary comprehension that iterates over the elements of row1. The for row in [row1] part ensures that we are iterating over a list containing row1. In this context, row represents each row of comma-separated values.

# 2. for i in range(0, len(row), 2): This part iterates over the indices of row with a step of 2. It means we are considering every second element in row, which corresponds to the keys in the dictionary.

# 3. row[i].strip(): row[i + 1].strip(): This is the key-value pair in the dictionary. row[i].strip() represents the key, and row[i + 1].strip() represents the value. The .strip() method is used to remove any leading or trailing whitespaces from both the key and the value.

# Putting it all together, the dictionary comprehension creates a dictionary where keys are obtained from even-indexed elements (after stripping whitespaces) and values are obtained from the corresponding odd-indexed elements (after stripping whitespaces).

# So, for example, if row1 is [' a', ' 100', ' b', ' 200', ' c', ' 300'], the resulting dict1 would be {'a': '100', 'b': '200', 'c': '300'} after stripping whitespaces.

# The same logic applies to dict2 for the second row (row2).


################### Next operator

# The next() function in Python is used to retrieve the next item from an iterator. 
# It can be used with various iterable objects like lists, tuples, sets, and, importantly, with iterators such as those returned by file objects and certain generator functions.
