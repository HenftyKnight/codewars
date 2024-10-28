def better_than_average(class_points: list, your_points: int):
    # First we will append out points to the class_points array
    class_points.append(your_points)
    
    # Get average total score 
    total_average_score = sum(class_points) / len(class_points)
    
    if your_points >= total_average_score:
        return True
    return False

print(better_than_average([2,3], 5))