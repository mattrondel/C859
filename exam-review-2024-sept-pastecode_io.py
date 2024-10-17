# Exam Review 2024 Sept

# Do those LABS
# Ch 2-14... all Labs!
# Ch 33 and 34... get to know the Prac Tests. Use them MORE than the Pre.

# Use Submit Mode and get them to 100%!!!
# PAY ATTENTION to the unit tests!
# ... then UNIT TEST more! Unit test, unit test, unit test!

# When you've gotten the Ch 33-34 Prac Tests to 100, go back and do each again.
# This time, try to think of 2-3 more unit tests that could be run on each question.

# Comp 1: Basic syntax and knowledge: operators, data types, etc
# Comp 2: Control Flow
# Comp 3: Modules and Files

# Comp 1: Basic syntax and knowledge: operators, data types, etc

# Data Types/Classes
# int
# floats
# bool # True, False... if x > 3
# str # ""
# list # [ ]
# dict # {key:value}
# tuple # () immutable, Python sees a,b,c as (a,b,c) --> return x, y -> return (x,y)
# set # {} all unique values, no order --> no indices, can't slice it, can't sort, can't reverse
# range # range()... container of a series of numbers --> range(start, stop, step), range(0, 5, 1) --> [0, 1, 2, 3, 4]
# file # open()... read(), readlines(), write()

# Operators
# = # assigns
# == # equality... asking a question, comparing
# +
# -
# *
# /
# % # modulo gives the whole number remainder, "how many things didn't fit since the last even division?"
# // # floor division... the last even division
# <
# >
# <=
# >=
# += # x += 1, x = x+1
# -=
# ** # raise to a power... pow(), math.pow()
# !=
# # keywords
# in # membership check... if myStr in myList
# not # if not myStr in myList
# and
# or # any one True will make the combo True... limit or to 2 or 3 conditions

# Comp 2
# Control Flow... the how and when
# IF statements... if, if/else, if/elif, if/elif/else
# LOOPS
# WHILE - a general purpose, an IF that repeats
# FOR - repeat action once for everything in some container
# for ___ in _someContainer_:
# for item in myList:
# for char in myStr:
# for key in myDict: # loop var holds key, we can use that to get the value myDict[key]
# for n in range(someNum):
# # if we want to know the index of something
# for i in range(0, len(myList), 1):
# for i, item in enumerate(myList):

# FUNCTIONS
# modular... a function has ONE specific job
# defining/writing a function vs calling
# print/output or return (or maybe something else)
# parameters are special variables for holding stuff coming into the function
# parameter vs argument

# def someFunction(x, y):
#     return x*y - 1
#
# if __name__ == "__main__":
#     input1 = int(input())
#     input2 = int(input())
#     # myAnswer = someFunction(input1, input2)
#     # print(myAnswer)
#     print(someFunction(input1, input2))

# See "tasks" in the last section of Ch 10, 11, 13, 14 for function writing practice
# CodingBat also has good function-based Python questions:
# https://codingbat.com/python

# Built-In Functions
# print()
# input()
# range() #constructor
# list()
# dict()
# str()
# int()
# float()
# len()
# chr()
# ord()
# min()
# max()
# sum()
# pow() # compare to math.pow()
# abs() # compare to math.fabs()
# enumerate()
# round() # compare to math.ceil(), math.floor()
# type() # myVar = "5" # print(type(myVar).__name__)
# help() # # help(str), help(str.isspace), help(__builtins__)
# dir() # print(dir(str))

# STRINGS
# be able to refer by index, and to slice
# myStr = "abcdef"
# # [start:stop:step]
# revStr = myStr[::-1]
# print(revStr)

# KNOW YOUR WHITESPACE
# " " space from spacebar
# # a whole of spaces in Unicode
# "\n" # new line return
# "\r" # carriage return
# "\t" # tab

# STRING METHODS
# myStr.format() # "Stuff I want to add in here like {} and {:.2f}".format(var1, var2)
# myStr.strip() # input().strip()
# myStr.split() # returns a list of smaller strings
# myStr.join(listOfStrings) # " ".join(listOfStrings)
# myStr.replace(subStr, newStr) # "remove"... myStr = myStr.replace(subStr, "")
# myStr.index(subStr) # return int index where found, or raise error
# myStr.find(subStr) # return int index where found, or -1 if not found
# myStr.count(subStr) # return int number of times found
# case methods: myStr.lower(), myStr.upper(), myStr.title(), myStr.capitalize()
# is/Boolean: myStr.islower(), isupper(), isspace(), isalpha(), isnumeric(), isdigit(), isalnum()
# myStr.startswith(subStr), myStr.endswith(subStr)

# LISTS
# be able to refer by index and to slice

# LIST METHODS
# # +
# myList.append(item)
# myList.insert(i, item)
# myList.extend(anotherList)
# # -
# myList.pop(i)
# myList.remove(item) # pop() by index, remove() by value
# myList.clear()
# # others
# myList.sort()
# myList.reverse()
# myList.count(item) # returns int number of times found
# myList.index(item)
# myList.copy()

# DICT
# use the key like an index []... then you don't really need DICT methods

# myDict[key] # get the value for that key, similar to myDict.get(key)
# myDict[key] = value # assign new value to key, similar to myDict.update({key:value})

# # membership check
# if ___ in myDict: # looks at keys
#
# # DICT METHODS
# myDict.keys() # all dict keys in a set-like object
# myDict.values() # all values in one container
#
# # # # membership check for value
# if ___ in myDict.values()

# MODULES
# math and csv

# MATH MODULE
# import math # FULL IMPORT
# math.factorial(x)
# math.ceil(x)
# math.floor(x)
# math.sqrt(x)
# math.pow(x, y)
# math.fabs(x)
# math.e
# math.pi
#
# # PARTIAL IMPORT
# from math import ceil
# # ceil(), not math.ceil()
# from math import floor, sqrt # floor(), sqrt()
# from math import * # sqrt(), floor(), pi
#
# # ALIAS IMPORT
# import math as m # m.floor(), m.sqrt()


# FILES
# modes: r, w, a

# READ MODE

# filename = input() # input1.txt
# with open(filename, "r") as f:
#     f.read() # return one big string of the whole file
#     f.readlines() # return a list of strings, where each line is a string
#     f.readline() # ITERATOR... I'll avoid this one but you can for line in f.readline();
#     f.write(someStr) # takes a single str argument to write into file

# with open("plain_text_file.txt", "r") as f:
#     contents = f.readlines()
#
# print(contents)
# for line in contents:
#     line = line.strip()
#     print(line)
# print(contents)

# CSV
import csv
with open("mock_data.csv", "r") as f1: # mockaroo.com
    # csv.reader(f), csv.reader(f, delimiter="\t") for a .tsv
    # contents = csv.reader(f1) # won't work the same, b/c it is an ITERATOR
    # but we can get around that
    contents = list(csv.reader(f1))

# print(contents)
# for row in contents[0:20]:
#     print(row)

# WRITE MODE
# ... is destructive! Even opening a file in write mode overwrites the previous contents!

# write out a new file with rows of data with .edu email address
# with open("output_data42.csv", "w") as f2:
#     for row in contents:
#         # write rows, as strings, where email is .edu
#         # email is at row[3]
#         if row[3].endswith(".edu"):
#             f2.write(",".join(row) + "\n")
#             # f2.write(f"{",".join(row)}\n")

# APPEND MODE
# let's read so we can check that last line for a line return or not?
# with open("append_to_this.txt", "r") as f3:
#     print(f3.readlines()) # ["Frodo\n", "Sam\n", "Merry"] -> no line return on last line here
with open("append_to_this.txt", "a") as f3:
    f3.write("\nPippin")

# In conclusion...
# Unit test, unit test, unit test

