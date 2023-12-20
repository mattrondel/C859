#this works for both PA and 
#https://learn.zybooks.com/zybook/WGUC859v4/chapter/34/section/4

# Accept three integer inputs for base (b1, b2) and height (h)
b1 = int(input())
b2 = int(input())
h = int(input())

# Calculate the trapezoid area
area = ((b1 + b2) / 2) * h

# Output the result in the required format
print(f'Trapezoid area: {area} square meters')
