from pydantic import BaseModel

class HouseData(BaseModel):
    transaction_date: float
    house_age: float
    distance_to_mrt: float
    num_convenience_stores: int
    latitude: float
    longitude: float
    