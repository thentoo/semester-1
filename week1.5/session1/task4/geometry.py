# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

    # Add distance() method here
    def distance(self, x_pos, y_pos):
        x_dist = abs(x_pos - self.x)
        y_dist = abs(y_pos - self.y)

        return (x_dist * x_dist) + (y_dist * y_dist)

    # Add distance_to() method here
    # (This will need a parameter representing another point)

    def distance_to(self, p):
        return self.distance(p.x, p.y)

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius) * (self.radius)
    
    def perimeter(self):
        return 2 * math.pi * (self.radius)

# Don't add any testing code to this file!
