# 🏠 House Price Prediction API

This is a FastAPI-based project designed for containerized deployment. The API can be used as a starting point for building machine learning or RESTful applications with Docker.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```

---

## ▶️ Run Locally (Without Docker)

To run the app locally using `uvicorn`, you'll need to install the required Python dependencies.

### Install Dependencies

```bash
pip install -r requirements.txt
```

Then, use the `start.sh` script to start the app:

```bash
./start.sh
```

Visit the app at:

```
http://127.0.0.1:8000/health
```

Expected output:

```json
{"status":"success","message": "System up"}
```

---

## 🐳 Run with Docker

To build and run the app using Docker, make the `run_docker.sh`executable:

```bash
chmod +x run_docker.sh
```
and then run

```bash
./run_docker.sh
```

Visit the app at:

```
http://127.0.0.1:8000/health
```

Expected output:

```json
{"status":"success","message": "System up"}
```
## 📄 Checkout the API docs at
```
http://127.0.0.1:8000/docs
```

---

## 📦 Requirements

- [Docker](https://www.docker.com/) — for containerized deployment
- [Python 3.8+](https://www.python.org/) — only required for local development

