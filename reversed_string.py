# This is what a normal soltuion works like
def solution(string):
    reversed_string=""
    for letter in range(len(string)-1,-1,-1):
        # print(string[letter])
        reversed_string += string[letter]
    return reversed_string

# Best Practice
def best_solution(string):
    return string[::-1]

print(best_solution('world'))