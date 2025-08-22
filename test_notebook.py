from testbook import testbook
import numpy as np

def test_values():
    with testbook('1_axis.ipynb', execute=True) as tb:
        average_monthly_coins = tb.value('float(average_monthly_coins)')
        assert np.isclose(average_monthly_coins, 23.3, atol=5e-2)

        average_monthly_coins_per_year = tb.value('list(average_monthly_coins_per_year)')
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
