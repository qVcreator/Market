from fastapi import APIRouter

from .product import router as product_router
from .account import router as account_router
from .payment import router as payment_router
from .transaction import router as transaction_router
from .user import router as user_router


router = APIRouter()
router.include_router(product_router)
router.include_router(account_router)
router.include_router(payment_router)
router.include_router(transaction_router)
router.include_router(user_router)

