import asyncio


async def my_coroutine():
    try:
        while True:
            await asyncio.sleep(0.1)
            print("Coroutine running")
    except asyncio.CancelledError:
        print("Cancelled my coroutine")


async def main():
    task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(3)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        pass


asyncio.run(main())
