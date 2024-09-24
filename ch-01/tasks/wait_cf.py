import asyncio


async def my_coroutine(delay):
    await asyncio.sleep(delay)
    print(f"Finished after {delay} seconds")


async def main():
    tasks = [asyncio.create_task(my_coroutine(i)) for i in range(1, 6)]
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_COMPLETED
    )
    print("First task completed", done)
    print("Remaining tasks", pending)


asyncio.run(main())
