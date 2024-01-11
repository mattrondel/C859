# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/6

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a function and have it condensed and simplifed and break this down step by step so I can understand this

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

input_id = input()

formatted_output = f"{input_id[:3]}-{input_id[3:5]}-{input_id[5:]}"
print(formatted_output)
