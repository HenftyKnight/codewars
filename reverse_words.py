"""
Complete the function that accepts a string parameter, 
and reverses each word in the string. All spaces in the 
string should be retained.

Time Complexity - O(n)
Space Complexity - O(n)
"""
text = "this is a text"
def reverse_words(text):
    text_list = text.split(" ")
    reverse_list = []
    for word in text_list:
        reverse_list.append(word[::-1])
    return ' '.join(reverse_list)

print(reverse_words(text))

"""
Split Words - Reverse - One Liner
return (' '.join(s[::-1] for s in text.split(' ')))
"""