from typing import List, Optional
from pydantic import BaseModel, Field


class PriceSeriesInput(BaseModel):
    symbol: str = Field(..., example="AAPL")
    prices: List[float] = Field(..., min_items=2, example=[150.0, 152.5, 149.0, 155.0, 158.0])


class MetricSummary(BaseModel):
    symbol: str
    sample_count: int
    mean_price: float
    max_price: float
    min_price: float
    total_return_pct: float
    volatility_std: float
    simple_moving_average_3: Optional[List[float]] = None
