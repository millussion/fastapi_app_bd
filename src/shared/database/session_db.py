from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine
import os
from dotenv import load_dotenv
import os
from sqlmodel import create_engine, Session

# Leer la variable de entorno inyectada por Docker Compose
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

