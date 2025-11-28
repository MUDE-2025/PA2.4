from testbook import testbook
import io
import numpy as np
import pytest

from max_even_squared import max_even_squared

def test_external_test_file():
    # Import inside the test to avoid pytest discovering it during collection
    import my_test  # for the solution, replace 'my_test' with 'my_test_solution'
  
    # Collect all test functions from my_test module
    test_functions = [
        getattr(my_test, name) 
        for name in dir(my_test) 
        if name.startswith('test_') and callable(getattr(my_test, name))
    ]
    
    # Check that exactly 5 tests are present
    assert len(test_functions) == 5, f"Expected 5 tests but found {len(test_functions)}"
    
    # Run each test function
    passed = 0
    failed = 0
    errors = []
    
    for test_func in test_functions:
        try:
            test_func()
            passed += 1
        except Exception as e:
            failed += 1
            errors.append(f"{test_func.__name__}: {str(e)}")
    
    # Check that all tests passed
    assert failed == 0, f"Some tests failed:\n" + "\n".join(errors)
    assert passed == 5, f"Expected 5 tests to pass but only {passed} passed"


if __name__ == "__main__":
    pytest.main([__file__, '-v'])