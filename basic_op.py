"""
Basic If-else loop for getting the value of operation
Python has a built in eval() function and string has 
a built in 'format(value1, operator, value2)' method
    
    eval("{}{}{}".format(value1, operator, value2))
"""
def basic_op(operator, value1, value2):
    if operator == '+':
        return (value1 + value2)
    elif operator == '-':
        return (value1 - value2)
    elif operator == '*':
        return (value1 * value2)
    elif operator == '/':
        return (value1 / value2)
    else:
        return f'Operator Unknown'
    
