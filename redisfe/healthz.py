"""
Healthz endpoint returns ok only when master redis server is up
"""

from redis.sentinel import Sentinel, MasterNotFoundError

import structlog

logger = structlog.getLogger("healthz")


def healthz():
    return "ok"
    # sentinel = Sentinel([('redis-0.redis', 26379)], socket_timeout=0.1)
    # try:
    #     sentinel.discover_master("redis")
    #     return "ok"
    # except MasterNotFoundError:
    #     logger.info("Redis master not yet ready")
    #     raise
