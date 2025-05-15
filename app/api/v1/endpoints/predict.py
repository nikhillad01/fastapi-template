from fastapi import APIRouter, Depends

from app.schemas import HouseData
from app.services.predictor import PredictorService
from app.dependencies import get_predictor_service

router = APIRouter()


@router.post("")
async def predict_price(
    data: HouseData,
    predictor: PredictorService = Depends(get_predictor_service)
):
    predicted_price = predictor.predict(data)
    return {"predicted_price_per_unit_area": round(predicted_price, 2)}
