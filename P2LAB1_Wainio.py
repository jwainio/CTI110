# Jack Wainio
# June 18th, 2024
# P1LAB1
# Measurement calculator

radius = float(input("What is the radius of the circle:"))

diameter = radius *2

import math

circumference = diameter * math.pi

circle_area = radius ** 2 * math.pi

print(f"The diameter of the circle is:{diameter}")
print(f"The circumference of the circle is:{circumference}")
print(f"The area of the circle is:{circle_area}")
