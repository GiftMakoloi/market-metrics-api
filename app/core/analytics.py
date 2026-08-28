import math
from typing import List, Dict, Any


class FinancialAnalyticsEngine:
    """Core domain engine for calculating statistical price metrics."""

    @staticmethod
    def calculate_mean(prices: List[float]) -> float:
        return sum(prices) / len(prices) if prices else 0.0

    @staticmethod
    def calculate_volatility(prices: List[float]) -> float:
        if len(prices) < 2:
            return 0.0
        mean = FinancialAnalyticsEngine.calculate_mean(prices)
        variance = sum((x - mean) ** 2 for x in prices) / (len(prices) - 1)
        return math.sqrt(variance)

    @staticmethod
    def calculate_moving_average(prices: List[float], window: int = 3) -> List[float]:
        if len(prices) < window:
            return []
        averages = []
        for i in range(len(prices) - window + 1):
            window_slice = prices[i : i + window]
            averages.append(round(sum(window_slice) / window, 2))
        return averages

    @classmethod
    def generate_report(cls, symbol: str, prices: List[float]) -> Dict[str, Any]:
        mean_val = cls.calculate_mean(prices)
        vol_val = cls.calculate_volatility(prices)
        sma = cls.calculate_moving_average(prices, window=3)

        initial_price = prices[0]
        final_price = prices[-1]
        total_return = ((final_price - initial_price) / initial_price) * 100

        return {
            "symbol": symbol.upper(),
            "sample_count": len(prices),
            "mean_price": round(mean_val, 2),
            "max_price": round(max(prices), 2),
            "min_price": round(min(prices), 2),
            "total_return_pct": round(total_return, 2),
            "volatility_std": round(vol_val, 2),
            "simple_moving_average_3": sma,
        }
