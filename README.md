# House Price Prediction API

This is a FastAPI-based application that predicts house prices per unit area based on various input features like house age, distance to MRT, etc.

## 🚀 Features

- REST API with FastAPI
- Machine learning model using scikit-learn
- Swagger UI for testing
- Dockerized deployment

## 🧰 Requirements

- Python 3.9+
- pip
- Optional: Docker

## 📦 Installation (Local)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Visit:  
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
   - Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🐳 Run with Docker

To build and run the app using Docker:

```bash
docker build -t house-price-prediction .
docker run -p 8000:8000 house-price-prediction
```

Then visit: [http://localhost:8000/docs](http://localhost:8000/docs)
