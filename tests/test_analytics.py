from app.core.analytics import FinancialAnalyticsEngine


def test_calculate_mean():
    prices = [10.0, 20.0, 30.0]
    assert FinancialAnalyticsEngine.calculate_mean(prices) == 20.0


def test_generate_report():
    prices = [100.0, 110.0, 105.0]
    report = FinancialAnalyticsEngine.generate_report("TEST", prices)

    assert report["symbol"] == "TEST"
    assert report["total_return_pct"] == 5.0
    assert report["sample_count"] == 3
