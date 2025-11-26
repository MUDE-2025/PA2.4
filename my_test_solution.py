import unittest

class TestMaxEvenSquare(unittest.TestCase):

    def test_regular_case(self):
        self.assertEqual(max_even_square([1, 2, 3, 4]), 16)

    def test_no_even_numbers(self):
        with self.assertRaisesRegex(ValueError, "no even numbers found"):
            max_even_square([1, 3, 5])

    def test_not_a_list(self):
        with self.assertRaisesRegex(TypeError, "not a list"):
            max_even_square("apple")

    def test_non_integer_in_list(self):
        with self.assertRaisesRegex(TypeError, "only integers are allowed"):
            max_even_square([1, 2, "apple"])

    def test_empty_list(self):
        with self.assertRaisesRegex(ValueError, "no even numbers found"):
            max_even_square([])
