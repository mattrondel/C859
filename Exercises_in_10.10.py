# test here:
# https://pythontutor.com/render.html#mode=display

# Task 1

# Complete the function to print the first X number of characters in the given string

# # Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
  #Student code goes here
  print(mystring[0:x])

# # expected output: WGU
printFirst('WGU College of IT', 3)

# # expected output: WGU College
printFirst('WGU College of IT', 11)


# test here:
# https://pythontutor.com/render.html#mode=display

# Task 2

# Complete the function to return the last X number of characters in the given string

# # Complete the function to return the last X number of characters
# # in the given string
def getLast(mystring, x):
# # Student code goes here
  return mystring[-x:]
# # expected output: IT
print(getLast('WGU College of IT', 2))

# # expected output: College of IT
print(getLast('WGU College of IT', 13))



# test here:
# https://pythontutor.com/render.html#mode=display

#Task 3

#Complete the function to return True if the word WGU exists in the given string otherwise return False

# Complete the function to return True if the word WGU exists in the given string
# otherwise return False
def containsWGU(mystring):
# Student code goes here
  if 'WGU' in mystring:
    return True
  else:
    return False

# expected output: True
print(containsWGU('WGU College of IT'))

# expected output: False
print(containsWGU('Night Owls Rock'))




# test here:
# https://pythontutor.com/render.html#mode=display

#Task 4

#Complete the function to print all of the words in the given string

# Complete the function to print all of the words in the given string
def printWords(mystring):
# Student code goes here
  words = mystring.split()

# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')    

# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')



# test here:
# https://pythontutor.com/render.html#mode=display

#Task 5 - done

#Complete the function to combine the words into a sentence and return a string

# Complete the function to combine the words into a sentence and return a string 
def combineWords(words):
# Student code goes here
  return ' '.join(words)

# expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))

# expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))




# test here:
# https://pythontutor.com/render.html#mode=display

#Task 6 - Done

#Complete the function to replace the word WGU with Western Governors University and print the new string

# Complete the function to replace the word WGU with Western Governors University
# and print the new string
def replaceWGU(mystring):
# Student code goes here
  print(mystring.replace('WGU', 'Western Governors University'))

# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')

# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')



# test here:
# https://pythontutor.com/render.html#mode=display

#Task 7  - STUMPED

#Complete the function to remove the word WGU from the given string ONLY if it's not the first word and return the new string

# Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string
def removeWGU(mystring):
# Student code goes here
  words = mystring.split()

def removeWGU(mystring):
  words = mystring.split()  # Split the string into a list of words
  if len(words) > 1 and words[0] != "WGU":  # Check if there are more than one words and the first word is not "WGU"
      words.remove("WGU")  # Remove "WGU" from the list if it's not the first word
  return " ".join(words)  # Join the words back into a string



# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))

# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))


# test here:
# https://pythontutor.com/render.html#mode=display

#Task 8 - DONE

#Complete the function to remove trailing spaces from the first string and leading spaces from the second string and return the combined strings

# Complete the function to remove trailing spaces from the first string
# and leading spaces from the second string and return the combined strings
def removeSpaces(string1, string2):
# Student code goes here
  return string1.strip() + string2.strip()

# expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))

# expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))


# test here:
# https://pythontutor.com/render.html#mode=display

#Task 9

#Complete the function to print the specified hourly rate with two decimals

# Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
# Student code goes here
  print(f'${rate:.2f}')

# expected output: $34.79
displayHourlyRate(34.789123)    

# expected output: $24.12
displayHourlyRate(24.123456)


# test here:
# https://pythontutor.com/render.html#mode=display

#Task 10 - needs work

#Complete the function to return the number of uppercase letters in the given string

# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
# Student code goes here
  print(countUpper(mystring))

# expected output: 4
print(countUpper('Welcome to WGU'))

# expected output: 2
print(countUpper('Hello, Mary'))
