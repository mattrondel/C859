# https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/1

# Derek
# -A similar question appeared in my OA, but instead of computing total distance traveled you had to compute total cost of stocks purchased. 
#
#Instructions:
# 
#Task:
#Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site. 
# Output the total distance traveled (this will be the output variable) to two decimal places (:.2f) given the following miles per employee commute to the job site. 
# Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:
#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#The solution output should be in the format
#Distance: total_miles_traveled
# 
#Sample Input/Output:
#If the input is
#1
#2
#3
#then the expected output is
#Distance: 197.33 miles

miles_per_employee = [15.62, 41.85, 32.67]

# add strip so shit doesnt break like so: int(input().strip())
int(input().strip())


Travel_A = int(input().strip())
Travel_B = int(input().strip())
Travel_C = int(input().strip())

# "the number of times an employee travels to a job site."
Total_Distance = (Travel_A * miles_per_employee [0]) + (Travel_B * miles_per_employee [1]) + (Travel_C * miles_per_employee [2])

# F strings refresher from corey: https://youtu.be/nghuHvKLhJA?t=129
# adding precision output to f strings (same video: https://youtu.be/nghuHvKLhJA?t=539

print(f"Distance: {Total_Distance:.2f} miles")


# Here's how it works:
# 
#     1. miles_per_employee is a list that contains the miles for each employee's commute.
#     2. The code takes three inputs (Travel_A, Travel_B, and Travel_C) representing the number of times each employee travels to a job site.
#     3. It calculates the total distance traveled by multiplying the number of travels for each employee by their corresponding miles per commute and summing them up.
#     4. Finally, it prints the result in the specified format with two decimal places using f-string formatting.
