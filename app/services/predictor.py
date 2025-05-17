import joblib
import pandas as pd
from app.schemas import HouseDataInput, HouseDataInternal

class PredictorService:
    def __init__(self):
        self.model_path = "ai_model/new_model.pkl"
        self.scaler_path = "ai_model/new_scaler.pkl"

        self.model = joblib.load(self.model_path)
        self.scaler = joblib.load(self.scaler_path)

    def convert_to_internal(self, data: HouseDataInput) -> HouseDataInternal:
        transaction_date = data.transaction_year + (data.transaction_month - 1) / 12
        return HouseDataInternal(
            transaction_date=transaction_date,
            house_age=data.house_age,
            distance_to_mrt=data.distance_to_mrt,
            num_convenience_stores=data.num_convenience_stores,
            latitude=data.latitude,
            longitude=data.longitude,
        )

    def predict(self, data: HouseDataInternal) -> float:
        input_df = pd.DataFrame([data.dict()])
        input_scaled = self.scaler.transform(input_df)
        prediction = self.model.predict(input_scaled)
        return prediction[0]
