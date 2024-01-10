# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/6

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a funtion and ha

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


# Need to verify this:

# Accept an integer input representing a 9-digit unformatted student identification number
identification_number = int(input("Enter a 9-digit identification number: "))

# Convert the integer to a string and format it with hyphens
formatted_identification = f"{identification_number // 1000000}-{(identification_number // 10000) % 100}-{identification_number % 10000}"

# Output the formatted identification number
print(formatted_identification)
