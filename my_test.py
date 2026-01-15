from max_even_squared import max_even_squared   #import the function to be tested

def test_regular_case():
    assert max_even_squared([1, 2, 3, 4]) == 16

def test_no_even_numbers():
    try:
        max_even_squared([1, 3, 5])
        assert False, "Expected an exception but none was raised"
    except ValueError as e:
        assert "no even numbers found" in str(e)

def test_not_a_list():
    try:
        max_even_squared("apple")
        assert False, "Expected an exception but none was raised"
    except TypeError as e:
        assert "not a list" in str(e)

def test_non_integer_in_list():
    try:
        max_even_squared([1, 2, "apple"])
        assert False, "Expected an exception but none was raised"
    except TypeError as e:
        assert "only integers are allowed" in str(e)

def test_empty_list():
    try:
        max_even_squared([])
        assert False, "Expected an exception but none was raised"
    except ValueError as e:
        assert "no even numbers found" in str(e)
