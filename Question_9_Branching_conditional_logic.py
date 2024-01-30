# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/9

# got wrong on PA

# https://www.youtube.com/watch?v=rfscVS0vtbw&t=6847s
# good example of what the PA might have:
# https://www.bitdegree.org/learn/best-code-editor/python-if-else-example-5


# Need to distinguash between if vs elif
# Don't forget the the colon after the IF elif statements!
# if temp < 33:
 #   state = "Frozen"

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a funtion and have it condensed and simplifed

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


temp = int(input().strip())
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
