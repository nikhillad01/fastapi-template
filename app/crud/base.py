from sqlalchemy.orm import Session
from typing import Generic, Type, TypeVar
from app.database.db_session import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=Base)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=Base)

class CRUDBase(Generic[ModelType,CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model
    
    def get_by_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id==id).first()
    