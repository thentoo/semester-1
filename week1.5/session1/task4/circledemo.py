# Week 1.5, Session 1: Task 4

import geometry

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

p = geometry.Point(0, 0)
radius = 1

c = geometry.Circle(p, radius)

print(f"Area: {c.area()}")
print(f"Perimeter: {c.perimeter()}")