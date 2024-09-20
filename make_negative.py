"""
My thinking process involved 
substracting the number from its twice value E.g 2 - (2*2) = -2
I didn't know we can directly return -number
"""
def make_negative(number):
    if number <=0 :
        return number
    return eval('{}{}{}'.format(number, '-', number*2))

"""
Best One Liner Solution
"""
def make_negative(number):
    return -abs(number)

number = [1, 10, -98, 0, -1]
for i in number:
    print(make_negative(i))