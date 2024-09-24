import asyncio
import time


async def my_coroutine(delay):
    await asyncio.sleep(delay)
    print(f"Finished after {delay} seconds")


async def main():
    start = time.time()
    print("Started main")
    tasks = [
        asyncio.create_task(my_coroutine(2)),
        asyncio.create_task(my_coroutine(1)),
        asyncio.create_task(my_coroutine(5)),
    ]
    await asyncio.gather(*tasks)
    print("Finished main")
    print(f"It took {time.time() - start} seconds")


asyncio.run(main())
