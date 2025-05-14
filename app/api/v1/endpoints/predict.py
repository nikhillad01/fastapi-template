from typing import List

from fastapi import APIRouter
from app.schemas import DummyRow

import pandas as pd


router = APIRouter()

@router.post("")
async def convert_to_dataframe(data: List[DummyRow]):
    df = pd.DataFrame([row.dict() for row in data])
    return df.head().to_dict(orient="records")
