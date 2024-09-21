https://learn.zybooks.com/zybook/WGUC859v4/chapter/26/section/1

https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=8

###################################################
# from: https://claude.ai/
###################################################

def miles_to_laps(miles):
    return miles / 0.25

# Get input from user
miles = float(input())

# Calculate laps
laps = miles_to_laps(miles)

# Print result
print('{:.2f}'.format(laps))


# This program does the following:

# The miles_to_laps() function takes miles as input and divides it by 0.25 (since one lap is 0.25 miles) to get the number of laps.
# We get the input from the user and convert it to a float.
# We call the miles_to_laps() function with the input.
# Finally, we print the result formatted to two decimal places.

# This solution should work for any input, including the example you provided (1.5 miles = 6.00 laps).

###################################################


# getting NameError: name 'number_of_laps' is not defined but why?
# also how would you figure out what to divide or muliply by? with info given : "One lap around a standard high-school running track is exactly 0.25 miles"


def miles_to_laps(user_miles):
    number_of_laps = user_miles * 4
    return number_of_laps
    

if __name__ == '__main__':
    user_miles = float(input())
    print(f'{number_of_laps:.2f}')
