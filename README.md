# Eliasib Cine API

Backend base para una aplicación móvil de películas, directores y categorías.

## Ejecutar con Docker

Requiere [Docker Desktop](https://www.docker.com/products/docker-desktop/).

```bash
docker build -t eliasib-cine-api .
docker run --rm -p 8000:8000 eliasib-cine-api
```

## Ejecutar con Python

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
fastapi dev app/main.py
```

Requiere Python 3.11+ para la instalación local.

## Documentación y endpoints

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>
- Health check: `GET /health`
- Películas: `GET /api/movies`, `GET /api/movies/{id}`, `POST /api/movies`
- Directores: `GET /api/directors`, `GET /api/directors/{id}`, `POST /api/directors`
- Categorías: `GET /api/categories`, `GET /api/categories/{id}`, `POST /api/categories`

## GitHub

```bash
git clone https://github.com/Anggel87/EliasCine-API.git
cd EliasCine-API
```
