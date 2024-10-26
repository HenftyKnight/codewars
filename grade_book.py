def score_to_grade():
    score_range_dictionary = {score: 'A' for score in range(90, 101)}
    score_range_dictionary.update({score: 'B' for score in range(80, 90)})
    score_range_dictionary.update({score: 'C' for score in range(70, 80)})
    score_range_dictionary.update({score: 'D' for score in range(60, 70)})
    score_range_dictionary.update({score: 'F' for score in range(0, 60)})

    return score_range_dictionary

def get_grade(s1, s2, s3):
    # Check if all inputs are valid numbers
    for arg in (s1, s2, s3):
        if not isinstance(arg, (int, float)):
            return f'Error: {arg} is not a number'
    
    # Calculate the average
    average_total = (s1 + s2 + s3) / 3
    
    # Generating the grading dictionary based on ranges
    grade_dict = score_to_grade()

    # Moving the score to the nearest integer
    average_score = int(average_total)

    # return grade based on average_total
    if average_score in grade_dict:
        return grade_dict[average_score]
    else:
        return f'Grade not found'
  
print(get_grade(53, 84, 72))
