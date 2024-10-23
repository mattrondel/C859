# CH 34 / PA question:
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/9


bottom message
    optional_safety_comment = "Caution: Hot!" == if temp = 212 else < 33 "Watch out for ice!" 

beaking it down
    safety_comment = "Caution: Hot!" if temp == 212 
    else "Watch out for ice!" if temp < 33
    else ""


  else:
    state = "Boiling"
   when building if,elif,else the else statements aka catch alls dont need a variable declaired just the msg part


# looks like what the exam had
# https://www.bitdegree.org/learn/best-code-editor/python-if-else-example-5

# course material:
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/5/section/4

# Socratica: If/Else in Python
# https://www.youtube.com/watch?v=f4KOjWS_KZs

# WGU Branches, Loops, and Functions
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d1b7b151-0134-46f9-899c-a8a900df6da4

# V4 Python Building Blocks - Branching
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2d9f6621-6f99-49b8-9cbe-ae2100e51fee

# WGU C859/D335:  Course Tips (link removed from course page on C859)
# https://srm--c.vf.force.com/apex/coursearticle?Id=kA03x000000l9u2CAA

# FreeCodeCamp Video: If Statements (1:40:06) 
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=6006s

# FreeCodeCamp Video: If Statements & Comparison (1:54:07) 
# https://www.youtube.com/watch?v=rfscVS0vtbw&t=6847s

# LinkedIn Learning; Python if/else - Conditionals
# https://www.linkedin.com/learning/python-essential-training-2/conditionals?u=2045532

# LinkedIn Learning; Python if/else - Conditional syntax
# https://www.linkedin.com/learning/python-essential-training-2/conditional-syntax?u=2045532

# got wrong on PA
# Remember when you see "possible variable name is __" equate the is as =
# need to learn more about mulitple if, else, else statements on one line

# https://www.youtube.com/watch?v=rfscVS0vtbw&t=6847s
# good example of what the PA might have:
# https://www.bitdegree.org/learn/best-code-editor/python-if-else-example-5
# or
# https://drbeane.github.io/python/pages/branching.html

# Derek
# -A similar question appeared in my OA, but instead of outputting a description of the water state based on the input water 
# temperature you had to output a letter grade based on the input number grade. 
# The solution and output were almost exactly the same.

# Need to distinguash between if vs elif
# Don't forget the the colon after the IF elif statements!
# if temp < 33:
 #   state = "Frozen"

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, 
# do this without a try and except and not with a funtion and have it condensed and simplifed

# Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. 
# Output a description of the water state based on the following scale:
#  
# If the temperature is below 33° F, the water is “Frozen”.
# If the water is between 33° F and 80° F (including 33), the water is “Cold”.
# If the water is between 80° F and 115° F (including 80), the water is "Warm".
# If the water is between 115° F and 211° (including 115) F, the water is “Hot".
# If the water is greater than or equal to 212° F, the water is “Boiling”.
# Additionally, output a safety comment only during the following circumstances:
#  
#  
# If the water is exactly 212° F, the safety comment is "Caution: Hot!"
# If the water temperature is less than 33° F, the safety comment is "Watch out for ice!"
# The solution output should be in the format
# water_state
# optional_safety_comment
#  
# Sample Input/Output:
# If the input is
# 118
# then the expected output is
# Hot
# Alternatively, if the input is
# 32
# then the expected output is
# Frozen
# Watch out for ice!


temp = int(input())
if temp < 33:
    state = "Frozen"
elif temp <= 80:
    state = "Cold"
elif temp <= 115:
    state = "Warm"
elif temp <= 211:
    state = "Hot"
else:
    state = "Boiling"
safety_comment = "Caution: Hot!\n" if temp == 212 else "Watch out for ice!\n" if temp < 33 else ""

print(state)
print(safety_comment, end='')

########################################################
##### Interestingly I can get away with the following:
########################################################

temp = int(input())
if temp < 33:
    state = "Frozen"
elif temp <= 80:
    state = "Cold"
elif temp <= 115:
    state = "Warm"
elif temp <= 211:
    state = "Hot"
else:
    state = "Boiling"
safety_comment = "Caution: Hot!" if temp == 212 else "Watch out for ice!" if temp < 33 else ""

print(state)
print(safety_comment)

# the bigest gotcha is the \n new lines

# Statements broken down my attmpt to figure it out by statements:

# If the temperature is below 33° F, the water is “Frozen”.
if temp < 33:
    state = "Frozen"

# If the water is between 33° F and 80° F (including 33), the water is “Cold”.
if temp <= 80 
    state = "Cold"

# If the water is between 80° F and 115° F (including 80), the water is "Warm".
if temp <= 115
    state = "Warm"

# If the water is between 115° F and 211° (including 115) F, the water is “Hot".
if temp <= 211
    state = "Hot"

########################################################
############ Dereks take on this is good too ###########
########################################################

temperature = int(input())

water_state = ""
safety_comment = ""

if temperature >= 212:
    water_state = "Boiling"
elif 115 <= temperature < 211:
    water_state = "Hot"
elif 80 <= temperature < 115:
    water_state = "Warm"
elif 33 <= temperature < 80:
    water_state = "Cold"
elif temperature < 33:
    water_state = "Frozen"
    safety_comment = "Watch out for ice!"

if temperature == 212:
    safety_comment = "Caution: Hot!"

print(water_state)
if safety_comment != "":
    print(safety_comment)
