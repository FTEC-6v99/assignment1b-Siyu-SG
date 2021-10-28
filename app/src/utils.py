# Create a function called calculate_avg_rating
# Parameters: the function should have one argument of type list of Review (i.e., the arg should be a list of Review objects)
# Returns: the function should return a float: the average of all raview ratings that are given in the list as an argument to this function.
#          The returned value should be rounded to the closest second decimal. Use the build-in round function: https://www.w3schools.com/python/ref_func_round.asp
#
# If the argument is an empty list, return 0.0
# for reference on exceptions, check the class notes here: https://github.com/FTEC-6v99/python-overview/blob/master/advanced/exceptions.py
#
# Make sure that you add type hints to the function paramter and return value

import typing as t
from app.src.Review import Review

def calculate_avg_rating(reviews:t.List[Review]) -> float: 
    if len(reviews) == 0: 
        return 0.0
    
    rating_sum = 0.0  #store the sum of all ratings 
    for review in reviews:        
        rating_sum += review.rating
    return round(rating_sum / len(reviews), 2)
