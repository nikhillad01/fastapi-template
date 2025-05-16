from pydantic import BaseModel, conint, confloat

class HouseDataInput(BaseModel):
    transaction_year: conint(ge=2000, le=2100)
    transaction_month: conint(ge=1, le=12)
    house_age: confloat(ge=0.0, le=100.0)
    distance_to_mrt: confloat(gt=0.0)
    num_convenience_stores: conint(ge=0)
    latitude: confloat(ge=-90.0, le=90.0)
    longitude: confloat(ge=-180.0, le=180.0)

class HouseDataInternal(BaseModel):
    transaction_date: confloat(ge=2000.0, le=2100.0)
    house_age: confloat(ge=0.0, le=100.0)
    distance_to_mrt: confloat(gt=0.0)
    num_convenience_stores: conint(ge=0)
    latitude: confloat(ge=-90.0, le=90.0)
    longitude: confloat(ge=-180.0, le=180.0)
