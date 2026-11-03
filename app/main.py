from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.router import api_router

app = FastAPI(
    title="Eliasib Cine API",
    version="1.0.0",
    description="API REST para películas, cartelera, salas, asientos, usuarios y boletos.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

assets_dir = Path(__file__).resolve().parent.parent / "assets"
app.mount("/media", StaticFiles(directory=assets_dir), name="media")


@app.get("/", tags=["health"])
async def root() -> dict[str, str]:
    return {"message": "Eliasib Cine API is running"}


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
