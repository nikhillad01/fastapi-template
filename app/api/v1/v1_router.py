from fastapi import APIRouter
from app.api.v1.endpoints import predict

v1_router = APIRouter()
v1_router.include_router(predict.router, tags=["Predict"], prefix="/predict")
