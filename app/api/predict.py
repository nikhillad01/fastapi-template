from fastapi import APIRouter, Depends

from app.schemas import HouseDataInput
from app.services.predictor import PredictorService
from app.dependencies import get_predictor_service

router = APIRouter()


@router.post("")
async def predict_price(
    data: HouseDataInput,
    predictor: PredictorService = Depends(get_predictor_service)
):
    internal_data = predictor.convert_to_internal(data)
    predicted_price = predictor.predict(internal_data)
    return {"predicted_price_per_unit_area": round(predicted_price, 2)}
