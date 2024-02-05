
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/12

########################################################################################################################
# This is the file read and can be complicated so I need to practice with this, need a break down step-by-step on this
########################################################################################################################

# Good video by Jerry 
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=333562d4-a5de-443e-a56b-ae1e01639376

# Issue with Zybooks is its the older way to do this and can conflict with what instructors teach and is also less efficent

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
