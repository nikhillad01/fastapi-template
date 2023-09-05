from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from app.api.deps import get_connection
from app.crud.crud_user import crud_user


router = APIRouter()


@router.get("/{id}")
async def get(id: int, db: Session = Depends(get_connection)):
    user = crud_user.get_by_id(db=db, id=id)
    return jsonable_encoder(user)
