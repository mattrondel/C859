# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/5

# Accepting five integer inputs
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

# Calculating sums
integer_sum = num1 + num2 + num3 + num4 + num5
float_sum = float(integer_sum)
string_sum = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

# Outputting the results
print(f"Integer: {integer_sum}\nFloat: {float_sum}\nString: {string_sum}")
