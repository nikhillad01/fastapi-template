from fastapi import APIRouter
from app.api import predict

router = APIRouter()
router.include_router(predict.router, tags=["Predict"], prefix="/predict")
