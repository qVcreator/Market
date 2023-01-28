from typing import List

from fastapi import APIRouter, status, Depends

from ..models import *
from ..services.product import ProductService

router = APIRouter(
    prefix="/products",
    tags=['products']
)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
async def add_product(
        product_data: CreateProduct,
        product_service: ProductService = Depends()
):
    return await product_service.create_product(product_data)


@router.get(
    '/{product_id}',
    status_code=status.HTTP_200_OK,
    response_model=Product
)
async def get_product(
        product_id: int,
        product_service: ProductService = Depends()
):
    return await product_service.get_product(product_id)


@router.get(
    '/all',
    status_code=status.HTTP_200_OK,
    response_model=List[Product]
)
async def get_all_products(
        product_service: ProductService = Depends()
):
    return await product_service.get_all_products()
