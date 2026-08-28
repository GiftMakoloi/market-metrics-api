from fastapi import APIRouter, HTTPException, status
from app.models.schemas import PriceSeriesInput, MetricSummary
from app.core.analytics import FinancialAnalyticsEngine

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy", "service": "Market Metrics API"}


@router.post("/analyze", response_model=MetricSummary, status_code=status.HTTP_200_OK)
def analyze_price_series(payload: PriceSeriesInput):
    if len(payload.prices) < 2:
        raise HTTPException(
            status_code=400, detail="Price series must contain at least 2 data points."
        )

    result = FinancialAnalyticsEngine.generate_report(payload.symbol, payload.prices)
    return result
