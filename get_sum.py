"""
output -
    (a,b) --> (a+b) (a + ... + b = (a...b))
    a and b are not ordered

Optimized solution - Usage
    sum()       - Summing the range
    range()     - to go from a ..b
    min(a,b)    - returns smaller number of a or b
    max(a,b)    - retruns greater number of a or b

Avoid complex and repetitive loop logic use built in pythons
optimized functions
"""

def get_sum(a,b):
    sum = 0
    if a > b:
        for i in range(b,a+1):
            sum += i
    else:
        for i in range(a, b+1):
            sum += i
    return sum

def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum(0,-1))