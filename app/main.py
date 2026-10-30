from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Eliasib Cine API",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api")


@app.get("/", tags=["health"])
async def root() -> dict[str, str]:
    return {"message": "Eliasib Cine API is running"}