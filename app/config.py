import os
from pydantic_settings import BaseSettings
from functools import lru_cache


class APISettings(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "local")


class LocalConfig(APISettings):
    DEVUG: bool = True


@lru_cache()
def get_api_settings() -> APISettings:
    return dict(local=LocalConfig())
