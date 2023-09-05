import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import get_api_settings
from app.utils.constants import APP_ENV


settings = get_api_settings()[APP_ENV]
engine = create_engine(settings.DB_CONNECTION_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
