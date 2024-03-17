# Zybooks exercise:
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/2

# Need this one fully explained as each operation is confusing

# got wrong on PA

# this problem is about functions
# refresher from corey https://www.youtube.com/watch?v=9Os0o3wzS_I

# Book Material:
# https://learn.zybooks.com/zybook/WGUC859v4/chapter/7/section/1

# Derek 
# -A similar question appeared in my OA, but instead of converting weight (oz, lbs, tons) you had to convert time (minutes, hours, days). 
# The solution and output were almost exactly the same.
Lab that deals with time is found here:
https://learn.zybooks.com/zybook/WGUC859v4/chapter/22/section/2

# The value 3600 is used because there are 60 seconds in a minute and 60 minutes in an hour. 
# Therefore, to convert seconds to hours, you divide the number of seconds by the total number of seconds in an 
# hour (60 seconds/minute * 60 minutes/hour = 3600 seconds/hour).

# if the PA follows this logic then this might be a similar problem:
# https://www.studytonight.com/python-howtos/how-to-convert-seconds-to-hours-minutes-and-seconds-in-python

# More importantly its still a function

# https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/

# need to know why use a funtion and the benefits of this or find out what this would look like without being a function
# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ


# Create a solution that accepts an integer input representing any number of ounces. 
# Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. 
# There are 16 ounces in a pound and 2,000 pounds in a ton.

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

##########################
##########################

SIMILARITIES COMPARED TO THE TWO VERSIONS


# OUNCES
def convert_ounces(ounces):
    tons = ounces // (16 * 2000)
    remaining_ounces = ounces % (16 * 2000)
    pounds = remaining_ounces // 16
    ounces = remaining_ounces % 16
    
    print(f"Tons: {tons}")
    print(f"Pounds: {pounds}")
    print(f"Ounces: {ounces}")

input_ounces = int(input())
convert_ounces(input_ounces)


# TIME
def ConvertSeconds(seconds):
    Hours = seconds // 3600
    remaining_seconds = seconds % 3600
    Minutes = remaining_seconds // 60
    Seconds = remaining_seconds % 60

    print(f"Hours: {Hours}")
    print(f"Minutes: {Minutes}")
    print(f"Seconds: {Seconds}")

inputseconds = int(input())
ConvertSeconds(inputseconds).


# FIRST LINE IS SMALL DIVIDED TO BIG
#NEXT LINE IS REMAINDER (%) FROM SMALL LOOKS LIKE THE FIRST LINE JUST WITH %
# THEN REMAINING // INTO THE WHOLE NUMBER AKA WHAT MAKES IT A SINGLE UNIT , 16 OZ IN LB OR 60 SECONDS TO HOUR
# COPY PASTE THIS LINE BUT SWAP OUT THE // FOR A %

#copy paste the output and reformat for fstring statements 
#TAKE THOSE VARIABLES AND INJECT THEM TO THE F STRINGS

#leave the funtion and create the input statement then the function callout 
# funtion callout is basically the funtion name with the varable you setup for the integer intput callout

DONT FORGET TO PUT IN THE INPUT VALUE IN THE FUNCTION!!!

# Breaking this down as it reads:
Create a solution that accepts an integer input representing any number of ounces. 
"integer input" and "input" "ounces"
input_ounces = int(input())

and with the obvious is build the print statement
then the expected output is

Tons: 1
Pounds: 2
Ounces: 3
to:
print(f"Tons: {Tons}")
print(f"Pounds: {Pounds}")
print(f"Ounces: {Ounces}")

Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value.

Question to understand is how do I know that this should be a function?



There are 16 ounces in a pound and 2,000 pounds in a ton.
