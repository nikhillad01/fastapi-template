
from functools import lru_cache
from app.services.predictor import PredictorService

@lru_cache()  # ensures service is created only once and reused for all requests (singleton)
def get_predictor_service() -> PredictorService:
    return PredictorService()
