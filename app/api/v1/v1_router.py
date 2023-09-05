from fastapi import APIRouter
from app.api.v1.endpoints import user

v1_router = APIRouter()
v1_router.include_router(user.router, tags=["Users"], prefix="/users")
