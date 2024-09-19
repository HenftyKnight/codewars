"""
Mumbling

1) string format (.-..-...-....)
2) capitalize first letter(.-_.-_..-_...)
3) the index-1 is how many lower case should follow

or best solution is to use python's enumerate() function
which gives you the char as well as its index
It returns a tuple which we will give us how many times
we need to print the sting and then will give us desired 
characters.

Then we will use the title or capitalize method to make
the first character plural and then format the string.
"""


def accum(st):
    list_st =  list(st)
    accum_list = []
    for index in range(len(list_st)):
        accum_list.append((list_st[index] * (index + 1)).capitalize())
    return '-'.join(accum_list)

def accum_enumerate(st):
    return '-'.join((char * i).title() for i, char in enumerate(st, 1))
        


print(accum_enumerate("abcd"))
print(accum_enumerate("RqaEzty"))