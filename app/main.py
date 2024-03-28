from fastapi import FastAPI, Depends

from routers import public, product


app = FastAPI()

app.include_router(
    public.router, prefix="/api/v1/public"
)

app.include_router(
    product.router, prefix="/api/v1/product"
)