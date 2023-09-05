from fastapi import FastAPI, Security
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.middleware.cors import CORSMiddleware
from app.database.db_session import SessionLocal
from app.api.v1.v1_router import v1_router


session = SessionLocal()

app = FastAPI(
    title="FastAPI template",
    version="1.0.0",
    # docs_url=None,
    description="template for all fastapi projects",
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
    return {"message": "server is running..."}


# @app.get("api/fastapi-template/v1/docs", include_in_schema=False)
# async def get_documentation():
#     return get_swagger_ui_html(
#         openapi_url="api/fastapi-template/v1/docs/openapi.json",
#         title="FastAPI template",
#     )


# @app.get("api/fastapi-template/v1/docs/openapi.json", include_in_schema=False)
# async def openapi():
#     return get_openapi(title="FastAPI template", version=app.version, routes=app.routes)


app.include_router(
    v1_router,
    prefix=f"/v1"
)
