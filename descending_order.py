"""
    Number
    Convert it into a list
    Descending Sort list
    Then merge

    strings can be sorted lexicographically in descending order.
    return int(''.join(sorted(str(num), reverse=True)))    
"""
def descending_order(num):
    if isinstance(num, int) and num >= 0:    
        string_num = str(num)
        list_of_numbers = [int(number) for number in str(string_num)]    
        list_of_numbers.sort(reverse = True)

        # Convert list of numbers into strings and then join and then convert 
        # it into integer
        string_num = ""
        for num in list_of_numbers:
            string_num += str(num)
        descending_number = int(string_num)
        return descending_number
    else:
        raise ValueError("Non-Negative integer expected")
