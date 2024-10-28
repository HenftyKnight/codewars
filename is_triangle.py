# How to make sure it is a triangle?
"""
TRIANGLE INEQUALITY THEOREM
: The sum of any two sides must be greater than the third side 
    : Conditions
        : a + b > c
        : a + c > b
        : b + c > a 
        : All sides should be greater than 0
"""

def is_triangle(a, b, c):
    # All the sides should be greater than 0
    if ((a == 0) or (b == 0) or (c == 0)):
        return False
    else:
        # Three conditions based on the Triangle Inequality Theorem
        if (((a + b) > c) and ((a + c) > b) and ((b + c) > a)):
            return True
        return False