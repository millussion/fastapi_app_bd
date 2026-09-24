# FastAPI & PostgreSQL API (Dockerized)

Una API RESTful robusta construida con **FastAPI**, utilizando **PostgreSQL** como base de datos, **SQLModel** como ORM y **Alembic** para la gestión y control de versiones de las migraciones de la base de datos. Todo el entorno está completamente contenedorizado utilizando **Docker** y **Docker Compose**.

##  Tecnologías Utilizadas

*   **Framework API:** [FastAPI](https://fastapi.tiangolo.com/)
*   **Base de Datos:** [PostgreSQL](https://www.postgresql.org/)
*   **ORM:** [SQLModel](https://sqlmodel.tiangolo.com/) (basado en SQLAlchemy y Pydantic)
*   **Migraciones:** [Alembic](https://alembic.sqlalchemy.org/)
*   **Contenedores:** [Docker](https://www.docker.com/) & Docker Compose
*   **Gestor de Base de Datos:** pgAdmin 4

##  Estructura del Proyecto

```text
fastapi_app_bd/
├── alembic/                  # Configuración y control de versiones de Alembic
│   ├── versions/             # Historial de migraciones SQL generadas
│   └── env.py                # Configuración de conexión para Alembic
├── src/
│   ├── models/
│   │   └── product_model.py  # Modelos de base de datos (SQLModel)
│   └── shared/
│       └── database/
│           └── session_db.py # Configuración del Engine y Sesión de la BD
├── main.py                   # Punto de entrada de la aplicación FastAPI y endpoints
├── Dockerfile                # Instrucciones de construcción de la imagen de la API
├── docker-compose.yml        # Orquestación de contenedores (API, DB)
├── requirements.txt          # Dependencias de Python
└── alembic.ini               # Archivo de inicialización de Alembic


# Guía Rápida de Ejecución (FastAPI + Docker + Alembic)

Sigue estos pasos en tu terminal para levantar el proyecto desde cero, crear la base de datos y generar las tablas correctamente. 

> **Nota:** Antes de empezar, asegúrate de estar en la raíz del proyecto (donde está el archivo `docker-compose.yml`) y verifica que la carpeta `alembic/versions/` esté completamente vacía de archivos `.py` para evitar conflictos.

## 1. Limpieza inicial
Borra cualquier contenedor, red o volumen previo que pueda tener errores o datos residuales:
```bash
docker compose down -v

