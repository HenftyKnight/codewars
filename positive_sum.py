def positive_sum(arr):
    sum = 0
    for number in arr:
        if number >=0:
            sum += number
    return sum

arr = [1,-4,7,12]
print(positive_sum(arr))

"""
Better to use the sum function
sum(x for x in arr if x > 0)
"""