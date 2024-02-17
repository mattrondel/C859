# Need this one fully explained as each operattion is confusing

# got wrong on PA

# Book Material:
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/7/section/1

# Derek 
# -A similar question appeared in my OA, but instead of converting weight (oz, lbs, tons) you had to convert time (minutes, hours, days). The solution and output were almost exactly the same.

# if the PA follows this logic then this might be a similar problem:
# https://www.studytonight.com/python-howtos/how-to-convert-seconds-to-hours-minutes-and-seconds-in-python

# More importantly its still a function

# https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/

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


# // means floor division it divides two numbers and rounds the result down to the nearest integer. SO THINK // MEANS REMAINDER ROUNDED DOWN "double forward slash divide remainder rounded down"
# The floor division operator // is used for this operation, and it returns an integer result without any decimal places

# % is modulus or modulo (aka MOD) its used to calculate the remainder of a division operation between two numbers like 5 % 2, 2 goes into 5 two times with a remander of 1, so THINK % MEANS REMAIDER ROUNDED DOWN or percentage means remainder rounded down

def convert_ounces(ounces):
    # Calculate tons, pounds, and remaining ounces
    #  16  oz in a pound and 2000 in a ton we are mulitpling them together becuase the input is in ounces, this is no different that asking how many minutes in a day, week, or month
    # the // floor division is there to divide and round down the function's parameter value placed in "(ounces):"
    tons = ounces // (16 * 2000)
    remaining_ounces = ounces % (16 * 2000)
    # notice that we just need to figure out these top two then work with the results
    pounds = remaining_ounces // 16
    ounces = remaining_ounces % 16
    # 16 is how many ounces in a pound

    # Output the result in the required format
    # this is just the case of copying the output they are asking for and formatting it with f" strings
    print(f"Tons: {tons}")
    print(f"Pounds: {pounds}")
    print(f"Ounces: {ounces}")

# Get input from the user
input_ounces = int(input())

# Call the function with the input above aka take the user input and send it to the function
convert_ounces(input_ounces)

#You can run this script, enter the number of ounces when prompted, and it will display the converted result in the specified format.
