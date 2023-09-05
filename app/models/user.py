import sqlalchemy
from sqlalchemy import Column, Integer, String
from app.database.db_session import Base

class User(Base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    