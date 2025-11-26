import unittest                                 #import unittest module for creating unit tests
from max_even_squared import max_even_squared   #import the function to be tested

class TestMaxEvenSquared(unittest.TestCase):

    # Test that the function returns 16 for input [1, 2, 3, 4]
    def test_regular_case(self):                                
        self.assertEqual(max_even_squared([1, 2, 3, 4]), 16)            

    def test_no_even_numbers(self):
        with self.assertRaisesRegex(### YOUR CODE HERE ###, "no even numbers found"):
            max_even_squared([1, 3, 5])

    # complete the following test methods
    def test_not_a_list(self):
        ### YOUR CODE HERE ###

    def test_non_integer_in_list(self):
        ### YOUR CODE HERE ###

    def test_empty_list(self):
        ### YOUR CODE HERE ###