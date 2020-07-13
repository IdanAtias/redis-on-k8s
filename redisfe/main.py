import asyncio

import structlog
import click
import uvicorn
from fastapi import FastAPI

from . import healthz
from . import api

logger = structlog.getLogger("redis-fe")

REDIS_FE_PORT = 7042


def create_app() -> FastAPI:
    app = FastAPI(
        title="redis-fe",
    )
    app.add_api_route(path="/healthz", endpoint=healthz.healthz, summary="redis-fe healthz endpoint")
    app.include_router(api.router, prefix="/api")
    return app


def create_server(app: FastAPI) -> uvicorn.Server:
    config = uvicorn.Config(app, port=REDIS_FE_PORT)
    config.load()
    return uvicorn.Server(config=config)


async def _main() -> None:
    app = create_app()
    server = create_server(app)
    logger.info("Starting...", port=REDIS_FE_PORT)
    await server.serve()


@click.command("redis-fe")
def main():
    asyncio.run(_main())
