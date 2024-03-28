from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from schema import Product

import db_on_mem

router = APIRouter()

@router.get("/")
async def get_all_products():
    return db_on_mem.db_product.get_products()

@router.post("/")
async def add_product(product: Product):
    db_on_mem.db_product.add_product(product)
    return f"{product.name} was added"
@router.put("/{product_id}")
async def update_product(product_id: str , product: Product):
    return db_on_mem.db_product.update_product(product_id, product)

@router.delete("/{product_id}")
async def delete_product(product_id: str):
    return db_on_mem.db_product.delete_product(product_id)