# Create a unit test method to test the calculate_avg_rating function created in the utils module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios

import unittest
from app.src.Review import Review
from app.src.ratingscalc import calculate_avg_rating

class testUtils(unittest.TestCase):

    #Null case
    def testNullReview(self):
        nullreview = calculate_avg_rating([])
        self.assertEqual(0.0, nullreview)

    #Check if the calculate avg is working       
    def test_Calc_Avg_Rating(self):
        reviews = [
                Review('Grill A','Best place','Would recommend to others', 4.0),
                Review('Grill A','Nice and chill place','Awesome food', 4.5), 
                Review('Grill A','Great service','The place was nice', 5.0),
        ]
        AvgRating = calculate_avg_rating(reviews)
        self.assertEqual(4.5, AvgRating)
