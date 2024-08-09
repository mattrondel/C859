
practice here:
https://replit.com/@mrondel/mainpy-1#main.py

# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/12

# WGU Chapter 14 (Files) (33 min)
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=aa186513-b69e-47ff-a359-ade2013b4768

# WGU Chapter 13 (Files) (19 min)  <-- This is now an optional chapter
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5222edde-40eb-45b3-9848-adde01176d0d

# WGU The Gotchas: Working with Files: Reading (25 min)
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=333562d4-a5de-443e-a56b-ae1e01639376

# WGU V4 Python Building Blocks - Files
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=97e48d86-7612-4703-9afe-ae49010debf4

# Corey Schafer: Reading + Writing to Files
# https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=25

# FreeCodeCamp Video: Reading Files (@ 3:12:41)
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=11561s

# FreeCodeCamp Video: Writing to Files (@ 3:21:26) 
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=12086s

########################################################################################################################
# This is the file read and can be complicated so I need to practice with this, need a break down step-by-step on this
########################################################################################################################

# Good video by Jerry 
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=333562d4-a5de-443e-a56b-ae1e01639376

# Try this lab
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/14/section/8

# Linked in:
# https://www.linkedin.com/learning/python-essential-training-18764650/opening-reading-and-writing?resume=false&u=2045532

# Derek
# * I got this wrong when I took the PA because I did not follow the instructions exactly. Instead of using the file.read() method I used the file.readlines() method.
# ==================================================
# -I had a different file related coding problem in my OA. My coding problem was to accept a string input, open a specified file, read the content of the
# file using the file.read() method, add the string input to the end of the content with a ' ' character in front of it, write the modified content back 
# to the file, and then output the modified content of the file. The solution and output were not the same as this question.

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a function and have it condensed and simplifed and break this down step by step so I can understand this

# Create a solution that opens a file and combines the words on each line into a sentence. Write the sentence string to the end of the text file "WordTextFile1.txt" on a new line. 
# Output the new contents of "WordTextFile1.txt". Use the open() function and write(), read() methods to interact with the text file.

# The solution output should be in the format:

# WordTextFile1.txt_contents
# word1
# word2
# word3 
# sentence
#  
# Sample Input/Output:
# If the file content is:

# WordTextFile1.txt

# then the expected output is
# cat
# chases
# dog
# cat chases dog
# Step 1: Open the file "WordTextFile1.txt" in read mode and read its contents, in the testing engine case you can't hard code anything so it has to accept any input 
# the "With" block closes the file once the with block exits

file_path = input()
with open(file_path, "r") as file:
    file_contents = file.read()

# Step 2: Split the contents into a list of words
words = file_contents.split()

# Step 3: Combine the words into a sentence
sentence = ' '.join(words)

# Step 4: Open the file again in append mode and write the sentence to the end
with open(file_path, "a") as file:
    file.write("\n" + sentence)

# Step 5: Open the file in read mode and print its updated contents
with open(file_path, "r") as file:
    updated_contents = file.read()

print(updated_contents)

#################################### Bottom used with 2/1 PA but displayed odd
file_path = input()
with open(file_path, "r") as file:
    words = file.read().split()
    sentence = ' '.join(words)

with open(file_path, "a") as file:
    file.write("\n" + sentence)

print(open(file_path, "r").read())

# This condensed version performs the same operations without using functions and without explicit error checking.
