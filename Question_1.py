#
#Instructions:
# 
#Task:
#Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site. 
# Output the total distance traveled to two decimal places (:.2f) given the following miles per employee commute to the job site. 
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

Travel_A = int(input())
Travel_B = int(input())
Travel_C = int(input())

Total_Distance = (Travel_A * miles_per_employee [0]) + (Travel_A * miles_per_employee [1]) + (Travel_A * miles_per_employee [2])

#print(f"{:.2f}")
print(Distance: {Total_Distance:.2f} miles)
