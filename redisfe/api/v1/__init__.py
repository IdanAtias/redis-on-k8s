from fastapi import APIRouter

from . import items


router = APIRouter()
router.include_router(items.router, prefix="/items", tags=["items"])
