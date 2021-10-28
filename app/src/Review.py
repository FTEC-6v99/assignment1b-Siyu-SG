# create a new class called Review
# the class must have the following properties/attributes:
# 1. restaurant: name of the restaurant
# 2. review_title: the title of the review
# 3. review_body: the body of the review
# 4. rating: a numeric rating from 1 to 5
#
# Your class constructor (__init__ function) must raise an Exception if
# rating provided was not between 1 and 5
#
# Use typing module to hint the class attributes

class Review:
    def __init__(self, restaurant: str, review_title: str, review_body: str, rating: int): 
        self.restaurant = restaurant
        self.review_title = review_title
        self.review_body = review_body
        if rating <= 0 or rating > 5:
            raise Exception('Rating needs to be between 1 to 5')
        self.rating = rating
