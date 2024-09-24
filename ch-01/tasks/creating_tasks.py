import asyncio


async def my_coroutine():
    print("Stating my coroutine")
    await asyncio.sleep(1)
    print("Finished my coroutine")


async def main():
    task = asyncio.create_task(my_coroutine())
    print("Main function continues")
    await task


asyncio.run(main())
