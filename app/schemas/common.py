from pydantic import BaseModel

class DummyRow(BaseModel):
    name: str
    age: int
    city: str
