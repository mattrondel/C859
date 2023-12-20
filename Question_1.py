def calculate_total_distance(travels_a, travels_b, travels_c):
  miles_per_employee = {
      'A': 15.62,
      'B': 41.85,
      'C': 32.67
  }

  total_miles_traveled = (travels_a * miles_per_employee['A'] + travels_b * miles_per_employee['B'] + travels_c * miles_per_employee['C'])

  return round(total_miles_traveled, 2)

# Get user input
travels_a = int(input(""))
travels_b = int(input(""))
travels_c = int(input(""))

# Calculate and display the result
total_distance = calculate_total_distance(travels_a, travels_b, travels_c)
print(f"Distance: {total_distance:.2f} miles")