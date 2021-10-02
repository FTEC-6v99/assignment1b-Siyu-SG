# Use unittest library to create a unit test method to test the calc_avg_rating function created in the ratingscalc module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios

import unittest
from app.src.Review import Review
from app.src.ratingscalc import calc_avg_rating
from app.src.utils import calculate_avg_rating

class testRatingCalc (unittest.TestCase):
    #Null case check
        def test_calc_avg_Null(self):
            reviews = {}
            actual = calc_avg_rating(reviews)
            self.assertTrue(actual == {})

        def test_calc_avg_valid(self):
            reviews = [
                Review("Grill A","Best place","Best food ever. Would recommend to others.", 4.0),
                Review("Grill A","Nice and chill place","Awesome food", 4.2), 
                Review("Grill B","Average","it was fine for what I ordered", 3.5),
                Review("Grill B","Okay place","It was average food", 3.6),
                Review("Grill C","Worst meal ever","Food was cold, undercooked", 1.0),
                Review("Grill C","Bad place","The server was not polite and the food was horrible.", 1.5),

            ]
            expectoutput = {
                "Grill A": 4.1,
                "Grill B": 3.55,
                "Grill C": 1.25
            }
            actual = calc_avg_rating(reviews)
            self.assertEqual(expectoutput, actual)
