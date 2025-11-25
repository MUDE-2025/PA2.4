from testbook import testbook # Ensure that the testbook package is installed


@testbook("4_tests.ipynb", execute=True)
def test_max_even(tb):
    # Get the function from the notebook
    max_even_square = tb.get("max_even_square")
    
    # --- non-list input ---
    try:
        max_even_square("apple")
    except TypeError as e:
        assert str(e) == "not a list"
    else:
        raise AssertionError("Expected TypeError: 'not a list'")

    # --- list with non-integer ---
    try:
        max_even_square([1, 3, "apple"])
    except TypeError as e:
        assert str(e) == "only integers are allowed"
    else:
        raise AssertionError("Expected TypeError: 'only integers are allowed'")

    # --- list with no even numbers ---
    try:
        max_even_square([1, 3, 5])
    except ValueError as e:
        assert str(e) == "no even numbers found"
    else:
        raise AssertionError("Expected ValueError: 'no even numbers found'")

    # --- valid list ---
    result = max_even_square([2, 3, 4])
    assert result == 16  # 4 squared
    
    print("All testbook tests passed!")