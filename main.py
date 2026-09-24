from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator
from sqlmodel import select, SQLModel
from src.models.product_model import Product
from src.shared.database.session_db import SessionDep, get_session, engine
from typing import Optional

app = FastAPI()

CATEGORIAS_EXISTENTES = {"mouses", "teclados", "tecnologia", "otros"}

class CreateProduct(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(ge=10000)
    quantity: int = Field(gt=0)
    category: str = Field(min_length=1)

    #minusculas
    @field_validator("name", "category", mode="before")
    @classmethod
    def to_lowercase(cls, value: str) -> str:
        if isinstance(value, str):
            return value.strip().lower()
        return value


@app.post("/product",status_code=status.HTTP_201_CREATED)
def create_product(product: CreateProduct, session: SessionDep):
    #cat. existentes
    if product.category not in CATEGORIAS_EXISTENTES:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La categoría '{product.category}' no existe. Categorías disponibles: {list(CATEGORIAS_EXISTENTES)}"
        )

    #duplicados
    existing = session.exec(
        select(Product).where(Product.name == product.name)
    ).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El producto '{product.name}' ya se encuentra registrado."
        )
    
    product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        quantity=product.quantity
    )
    session.add(product)
    session.commit()
    session.refresh(product)

    return product

@app.get("/product", status_code=status.HTTP_200_OK)
def get_products(session: SessionDep):
    products = session.exec(
        select(Product)
    ).all()

    return products

@app.delete('/product/{id}', status_code=status.HTTP_200_OK)
def delete_product(product_id: int, session: SessionDep):
    product = session.exec(
            select(Product).where(Product.id == product_id)
    ).one()
    session.delete(product)
    session.commit()