# Create a function called: calc_avg_rating
# Parameters: the function should receive 1 parameter: a list of review objects
#             Remember a list can contain duplicates, so you can expect multiple reviews for the same restaurant
# Returns: the function should return a dictionary with restaurant name as key and average rating as value
#
#
# If the list of reviews is empty, return an empty dictionary
# Make sure that you add type hints to the function paramter and return value

import typing as t
from app.src.Review import Review
from app.src.utils import calculate_avg_rating


def calc_avg_rating(reviews: t.List[Review]) -> t.Mapping[str, float]:
    if reviews == {}: #check the reviews if it is empty
        return {} 

    review_R: dict[str, list[Review]] = {}  # set up two lists
    rating_R: dict[str, float] = {}

    for review in reviews:
        if review_R.get(review.restaurant) is None:
            review_R[review.restaurant] = [review]            
        elif review_R.get(review.restaurant) is not None:
                review_R.get(review.restaurant).append(review)

    for restaurant, reviews in review_R.items():
        rating_R[restaurant] = calculate_avg_rating(reviews)
    return rating_R
