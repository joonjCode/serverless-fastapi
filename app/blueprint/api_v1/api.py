from fastapi import APIRouter
from .endpoints import services


router = APIRouter()
router.include_router(services.router, prefix = '/services', tags = ['Services'])