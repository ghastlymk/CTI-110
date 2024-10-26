# Landon Graessle
# 3 October 2024
# P2LAB1
# Calculate the circumference, diameter, and area of a circle

# Get values based off user input of radius

radius = float(input("What is the radius of the circle? "))
pi = float(3.14159)
diameter = float(radius * 2)
circumference = float(radius * pi * 2)
area = float(pi * radius ** 2)

# Print caluclated values

print(f"The diameter of the circle is {diameter:.2f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
