import os
from typing import Dict
from pydantic_settings import BaseSettings
from functools import lru_cache


class APISettings(BaseSettings):
    POSTGRES: Dict = {
        "user": os.getenv("DB_USERNAME", "postgres"),
        "pw": os.getenv("DB_PASSWORD", "admin"),
        "db": os.getenv("DB_NAME", "fastapitemplate_db"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "5432"),
    }

    DB_CONNECTION_URI: str = (
        "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
    )

    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "local")


class LocalConfig(APISettings):
    DEVUG: bool = True


@lru_cache()
def get_api_settings() -> APISettings:
    return dict(local=LocalConfig())
