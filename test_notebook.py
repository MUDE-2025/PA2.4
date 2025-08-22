from testbook import testbook
import numpy as np

def test_values():
    with testbook('1_axis.ipynb', execute=True) as tb:
        average_monthly_coins = tb.ref('average_monthly_coins')
        assert np.isclose(average_monthly_coins, 23.3, atol=1e-1)

        average_monthly_coins_per_month = tb.ref('average_monthly_coins_per_month')
        expected_per_month = np.array([23.8, 22.0, 24.2])
        assert np.allclose(average_monthly_coins_per_month, expected_per_month, atol=1e-1)

        average_coins_september = tb.ref('average_coins_september')
        assert np.isclose(average_coins_september, 46.7, atol=1e-1)

        average_coins_january = tb.ref('average_coins_january')
        assert np.isclose(average_coins_january, 23.7, atol=1e-1)

        max_coins_month = tb.ref('max_coins_month')
        assert np.isclose(max_coins_month, 53.0, atol=1e-1)

        max_coins_year = tb.ref('max_coins_year')
        assert np.isclose(max_coins_year, 290.0, atol=1e-1)
