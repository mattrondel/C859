# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/9

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a funtion and have it condensed and simplifed

# Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. Output a description of the water state based on the following scale:
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

# Need to test:
temp = int(input())
state = (
    "Frozen" if temp < 33 else
    "Cold" if temp <= 80 else
    "Warm" if temp <= 115 else
    "Hot" if temp <= 211 else
    "Boiling"
)
safety_comment = "Caution: Hot!" if temp == 212 else "Watch out for ice!" if temp < 33 else ""

print(state)
print(safety_comment)

