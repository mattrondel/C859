# test.txt
# 1) This is a test file
# 2) With multiple lines of data...
# 3) Third line
# 4) Fourth line
# 5) Fifth line
# 6) Sixth line
# 7) Seventh line
# 8) Eighth line
# 9) Ninth line
# 10) Tenth line

# read vs readline vs readlines
# read() Reads all the elements of the file 
# readline() only reads the first line
# readlines() Makes a list of strings

file_path = input()
with open(file_path, 'r') as file:
  file_contents = file.readlines()
  print(file_contents)

# output of read() would be
# 
# test.txt
# 1) This is a test file
# 2) With multiple lines of data...
# 3) Third line
# 4) Fourth line
# 5) Fifth line
# 6) Sixth line
# 7) Seventh line
# 8) Eighth line
# 9) Ninth line
# 10) Tenth line
  
# output with readlines would be:
# test.txt
# ['1) This is a test file\n', '2) With multiple lines of data...\n', '3) Third line\n', '4) Fourth line\n', '5) Fifth line\n', '6) Sixth line\n', '7) Seventh line\n', '8) Eighth line\n', '9) Ninth line\n', '10) Tenth line']
