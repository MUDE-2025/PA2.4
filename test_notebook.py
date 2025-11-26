from testbook import testbook
import unittest
import io
import sys
import numpy as np

def test_values():
    with testbook('1_axis.ipynb', execute=True) as tb:
        average_monthly_coins = tb.value('float(average_monthly_coins)')
        assert np.isclose(average_monthly_coins, 23.3, atol=5e-2)

        average_monthly_coins_per_year = tb.value('[float(x) for x in average_monthly_coins_per_year]')
        expected_per_month = np.array([23.8, 22.0, 24.2])
        assert np.allclose(average_monthly_coins_per_year, expected_per_month, atol=5e-2)

        average_coins_september = tb.value('float(average_coins_september)')
        assert np.isclose(average_coins_september, 46.7, atol=5e-2)

        average_coins_january = tb.value('float(average_coins_january)')
        assert np.isclose(average_coins_january, 23.7, atol=5e-2)

        max_coins_month = tb.value('float(max_coins_month)')
        assert np.isclose(max_coins_month, 53.0, atol=5e-2)

        max_coins_year = tb.value('float(max_coins_year)')
        assert np.isclose(max_coins_year, 290.0, atol=5e-2)



def test_assert():
    with testbook('3_asserts.ipynb', execute=True) as tb:
        x = tb.value('x')
        assert np.isclose(x, 1.0, atol=1e-2) or np.isclose(x, 0.0, atol=1e-2), 'x should be 1 or 0'


class TestNotebookAssertions(unittest.TestCase):
    def test_assert2(self):
        with testbook('3_asserts.ipynb', execute=False) as tb:
            with self.assertRaises(AssertionError):
                tb.execute_cell(2)


class TestNotebookTestOutput(unittest.TestCase):

    def test_notebook_test_output(self):
        """
        Runs the notebook test cell and checks that it outputs as expected.
        """

        # Capture stdout
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            with testbook('3_asserts.ipynb', execute=False) as tb:
                tb.execute_cell(2)
        except Exception as e:
            self.fail(f"Notebook test cell raised an exception: {e}")
        finally:
            sys.stdout = sys_stdout
        output = captured_output.getvalue()
        
        # Check that the output contains the expected string
        # For unittest in a notebook, usually it prints "OK" when tests pass
        self.assertIn("OK", output, f"Expected 'OK' in output but got:\n{output}")


if __name__ == "__main__":
    unittest.main()