from testbook import testbook
import unittest
import io
import numpy as np

from max_even_squared import max_even_squared

class TestExternalPyTest(unittest.TestCase):

    def test_external_test_file(self):
        # Import inside the test to avoid pytest discovering it during collection
        from my_test import TestMaxEvenSquared  # for the solution, replace 'my_test' with 'my_test_solution'
      
        # Capture stdout so we can inspect test runner output
        captured_output = io.StringIO()
        runner = unittest.TextTestRunner(stream=captured_output, verbosity=2)

        # Load all tests from the original test class
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(TestMaxEvenSquared)

        # Run the test suite
        result = runner.run(suite)

        # Get the output
        output = captured_output.getvalue()

        # Check that all tests passed
        if not result.wasSuccessful():
            self.fail(f"Original test class failed:\n{output}")

        # Optionally check that output contains "OK"
        self.assertIn("OK", output, f"Expected 'OK' in output but got:\n{output}")


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
