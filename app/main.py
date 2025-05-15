from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.v1_router import v1_router


app = FastAPI(
    title="House Price Prediction API",
    version="1.0.0",
    description="APIs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status":"success","message": "System up"}


@app.get("api/house-price-prediction/v1/docs", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(
        openapi_url="api/house-price-prediction/v1/docs/openapi.json",
        title="House Price Prediction API",
    )


@app.get("api/house-price-prediction/v1/docs/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(title="House Price Prediction API", version=app.version, routes=app.routes)


app.include_router(
    v1_router,
    prefix=f"/v1"
)
