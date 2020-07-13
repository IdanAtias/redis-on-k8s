"""
Healthz endpoint returns ok only when master redis server is up
"""
import structlog

from fastapi import APIRouter
from redis.sentinel import Sentinel, MasterNotFoundError

router = APIRouter()
logger = structlog.getLogger("healthz")


@router.get(
    "",
    summary="redis-fe health check endpoint",
    response_model=str,
)
def healthz():
    sentinel = Sentinel([('redis-0.redis', 26379)], socket_timeout=0.1)
    try:
        sentinel.discover_master("redis")
        return "ok"
    except MasterNotFoundError:
        logger.info("Redis master not yet ready")
        raise
