from fastapi import APIRouter, Depends

from db_on_mem import db_product

router = APIRouter()

@router.get("/")
async def get_testroute():
    return "OK"

@router.get("/products")
async def get_all_products():
    return db_product.get_products()