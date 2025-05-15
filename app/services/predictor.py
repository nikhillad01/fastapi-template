import joblib
import pandas as pd
from app.schemas.prediction import HouseData

class PredictorService:
    def __init__(self):
        self.model_path = "ai_model/new_model.pkl"
        self.scaler_path = "ai_model/scaler.pkl"

        self.model = joblib.load(self.model_path)
        self.scaler = joblib.load(self.scaler_path)

    def predict(self, data: HouseData) -> float:
        input_df = pd.DataFrame([data.dict()])
        input_scaled = self.scaler.transform(input_df)
        prediction = self.model.predict(input_scaled)
        return prediction[0]
