# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/2

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

# Call the function with the input
convert_ounces(input_ounces)


#You can run this script, enter the number of ounces when prompted, and it will display the converted result in the specified format.
