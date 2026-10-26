# Week 1.5, Session 1: Task 3

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



# Finally, add code here to demonstrate use of Point
p = Point(0, 0)
q = Point(1, 2)

print(p.distance_to(q))
