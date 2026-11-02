# Eliasib Cine API

API REST para películas, cartelera, salas, asientos, usuarios y boletos sobre MySQL peliculasdb.

## Ejecutar con Docker Compose

Requiere Docker Desktop.

    docker compose up --build

Este comando construye la API y levanta los dos contenedores:

- API: http://localhost:8000
- MySQL Docker: localhost:3307

El esquema database/schema.sql se ejecuta automáticamente al crear el volumen de MySQL.

Para detener los contenedores:

    docker compose down

Para reiniciar la base desde cero, eliminando sus datos:

    docker compose down -v
    docker compose up --build

## Rutas útiles

- Swagger: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Health check: GET /health
- API: /api

Cada recurso expone GET, GET /{id}, POST, PUT /{id} y DELETE /{id}.

Recursos: movies, directors, categories, users, auditoriums, seats, movie-screenings y tickets.

Documentación detallada: docs/api-dictionary.html.
