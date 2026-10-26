# Another bad class implementation

# What does the runtime error mean?
# How do we fix the code?

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate
    
    def distance_squared(self, to_x, to_y):
        x_dist = abs(to_x - self.x)
        y_dist = abs(to_y - self.y)

        return (x_dist * x_dist) + (y_dist * y_dist)


p = Point(1.5, 2.0)
print(p.x)
print(p.y)

print(p.distance_squared(1, 2))