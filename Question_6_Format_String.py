# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/6

# "without hard-coded information, allowing the function to handle different input values"


#Does not work::
def format_student_id(student_id):
    # Convert the integer to a string
    student_id_str = str(student_id)
    
    # Format the string as per the required pattern
    formatted_id = f"{student_id_str[:3]}-{student_id_str[3:5]}-{student_id_str[5:]}"
    
    return formatted_id

# Sample Input
input_id = 154175430

# Output
output_id = format_student_id(input_id)
print(output_id)

#This code defines a function format_student_id that takes an integer input, converts it to a string, and then formats it according to the specified pattern. The sample input is provided, and the output is printed, producing the desired result.
