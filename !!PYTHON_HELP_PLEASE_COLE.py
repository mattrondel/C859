https://learn.zybooks.com/zybook/WGUC859v4/chapter/26/section/1
# getting NameError: name 'number_of_laps' is not defined but why?
# also how would you figure out what to divide or muliply by? with info given : "One lap around a standard high-school running track is exactly 0.25 miles"


def miles_to_laps(user_miles):
    number_of_laps = user_miles * 4
    return number_of_laps
    

if __name__ == '__main__':
    user_miles = float(input())
    print(f'{number_of_laps:.2f}')
