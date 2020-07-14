from datetime import datetime
import structlog
import asyncio
import aiohttp
import os

logger = structlog.get_logger("test")

NUM_ITEMS = 100

EIP = os.environ["EIP"]  # external ip should be set as an env variable
BASE_URL = f"http://{EIP}/api/v1"
URL = BASE_URL + "/items/{key}"


async def write():
    async with aiohttp.ClientSession() as session:
        for i in range(NUM_ITEMS):
            key = f"key-{i}"
            value = f"value-{i}"
            await session.put(URL.format(key=key), json={'value': value})


async def read():
    async with aiohttp.ClientSession() as session:
        for i in range(NUM_ITEMS):
            key = f"key-{i}"
            async with session.get(URL.format(key=key)) as resp:
                json_resp = await resp.json()
                assert json_resp["value"] == f"value-{i}"


async def main():
    start_write_time = datetime.now()
    logger.info("Writing items to DB", time=str(start_write_time), num_items=NUM_ITEMS)
    await write()
    end_write_time = datetime.now()
    writing_total_time = end_write_time - start_write_time
    logger.info("Done writing items to db", took=writing_total_time.seconds)

    start_read_time = datetime.now()
    logger.info("Reading items from DB", time=str(start_read_time), num_items=NUM_ITEMS)
    await read()
    end_read_time = datetime.now()
    reading_total_time = end_read_time - start_read_time
    logger.info("Done reading items from db", took=reading_total_time.seconds)

    total_time_in_sec = writing_total_time.seconds + reading_total_time.seconds
    logger.info("Done", overall_took=total_time_in_sec)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
