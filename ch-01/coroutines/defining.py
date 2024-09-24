import asyncio


async def my_coroutine():
    print("Started my coroutine")
    await asyncio.sleep(1)
    print("Finished my coroutine")


async def main():
    await my_coroutine()


asyncio.run(main())
