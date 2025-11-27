from max_even_squared import max_even_squared   #import the function to be tested

class TestMaxEvenSquared():

    # Test that the function returns 16 for input [1, 2, 3, 4]
    def test_regular_case():                                
        assert max_even_squared([1, 2, 3, 4]) == 16            

    def test_no_even_numbers():
        try:
            max_even_squared([1, 3, 5])
            assert False, "Expected an exception but none was raised"
        except ### YOUR CODE HERE ### as e:
            assert "no even numbers found" in str(e)

    # complete the following test methods
    def test_not_a_list():
        ### YOUR CODE HERE ###

    def test_non_integer_in_list():
        ### YOUR CODE HERE ###

    def test_empty_list():
        ### YOUR CODE HERE ###