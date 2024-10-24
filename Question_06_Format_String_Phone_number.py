# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/6

THIS IS A THREE PART BECAUSE YOU CANT SLICE INTEGERS ONLY STRINGS

# Derek notes
# -A similar question appeared in my OA, but instead of a 9-digit student ID you had to format an 11-digit phone number. 
# The solution and output were almost exactly the same.
# this is probaly the lab used in the PA https://learn.zybooks.com/zybook/WGUC859v4/chapter/33/section/6

# THIS UTILIZES SLICING NEED TO READ UP ON THIS MORE
# https://www.youtube.com/watch?v=ajrtAuDg3yw&t=453s

# Task:
# Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. Output the identification number as a string with no spaces.
# The solution output should be in the format
# 111-22-3333
#  
# Sample Input/Output:
# If the input is
# 154175430
# then the expected output is
# 154-17-5430

# Create a solution that accepts an integer input as a a 9-digit unformatted student identification number (or 11-digit phone number)
# Funny part of this is we will be using string slicing so don't use int(input()) just the plain vanilla string input()
input_id = input()

# you need to send the sliced string somewhere as you can't directly print a a sliced string 
# copy paste and edit the desired output as f strings 
# string Slicing is done by [START:END:STEP] but we wont be using the :STEP part but the slicing is added within the {} next to the variable for the string we are slicing
# Pro-tip #1: for slicing, copy the sample input and shift arrow key and count from 0 up to get the desired range 
# again its [START:STOP]
# Stop is always one number more than what you want aka non-inclusive
# for example if you want 154 out of 154175430 count one number higher than the 4 and thats what you need
# Protip #2: If you are trying to get one charater and the rest of the line you put the start charater then leave the stop as blank like so [5:] like if you wanted 5430 out of 154175430

formatted_id = (f"{input_id[0:3]}-{input_id[3:5]}-{input_id[5:]}")
# You can remove the () but you don't have to like so:
# formatted_output = f"{input_id[:3]}-{input_id[3:5]}-{input_id[5:]}"
# print the formatted and sliced string
print(formatted_output)

# Slicing is done by [START:END:STEP]
# Note that END is non-inclusive meaning it won't be included with your slice
# So if your you want 1-4 your slice should be [1:5]
# alternativly if you want a number to the end use [4:]

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#            0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#          -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# print my_list[1:3]
# this would output 12

# If you are trying to take a phone number and output it like from 16617226300 you would do something like this:
#phone = str(16617226300)

#formatted_input = f"{phone[0:1]}-{phone[1:4]}-{phone[4:7]}-{phone[7:]}"

#print(formatted_input)

# Things to remeber:
# Says integer input but this is "string" slicing
# You can't go directly from slicing to printing you need to slice then send to variable then print

REMEMBER:
COPY THE OUTPUT WITH BOTH WHAT IS DESIRED THEN WITHOUT ADDITIVES THEN COUNT
