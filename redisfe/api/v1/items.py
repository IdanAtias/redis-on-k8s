from typing import List
import structlog

from fastapi import APIRouter
from redis.sentinel import Sentinel

router = APIRouter()
logger = structlog.getLogger("redis-items")


sentinel = Sentinel([('redis-0.redis', 26379)], socket_timeout=0.1)


@router.put(
    "/{key}",
    summary="Create redis item",
)
def add(key: str, value: str):
    logger.info("Adding redis item", key=key, value=value)
    master = sentinel.master_for("redis")  # slaves are read-only; use master for writes
    master.set(key, value)


@router.get(
    "/{key}",
    summary="Get redis item",
    response_model=str,
)
def get(key: str):
    logger.info("Getting redis item", key=key)
    slave = sentinel.slave_for("redis")  # use slave for reads
    value = slave.get(key)
    logger.info("Got redis item", key=key, value=value)
    return value


@router.get(
    "",
    summary="List all redis items",
    response_model=List[str],
)
def get_all():
    logger.info("Listing redis items")
    items = []
    slave = sentinel.slave_for("redis")
    for key in slave.keys():
        value = slave.get(key)
        items.append(f"{key}: {value}")
    return items
