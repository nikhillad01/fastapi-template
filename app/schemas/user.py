from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    name: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
