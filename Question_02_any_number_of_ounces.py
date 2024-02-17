# Need this one fully explained as each operattion is confusing

# got wrong on PA

# Derek 
# -A similar question appeared in my OA, but instead of converting weight (oz, lbs, tons) you had to convert time (minutes, hours, days). The solution and output were almost exactly the same.

# need to know why use a funtion and the benefits of this or find out what this would look like without being a function
# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ

# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/2

# Help me solve and understand this python problem and also solve it so it can accept any input, remove any error checking, do this without a try and except and not with a function and have it condensed and simplifed and break this down step by step so I can understand this

# Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound and 2,000 pounds in a ton.
# The solution output should be in the format
# Tons: value_1
# Pounds: value_2
# Ounces: value_3
#  
# Sample Input/Output:
# If the input is
# 32035
# then the expected output is
# Tons: 1
# Pounds: 2
# Ounces: 3


def convert_ounces(ounces):
    # Calculate tons, pounds, and remaining ounces
    tons = ounces // (16 * 2000)
    remaining_ounces = ounces % (16 * 2000)
    pounds = remaining_ounces // 16
    ounces = remaining_ounces % 16

    # Output the result in the required format
    print(f"Tons: {tons}")
    print(f"Pounds: {pounds}")
    print(f"Ounces: {ounces}")

# Get input from the user
input_ounces = int(input())

# Call the function with the input <--- need to understand this part from chat
convert_ounces(input_ounces)


#You can run this script, enter the number of ounces when prompted, and it will display the converted result in the specified format.
