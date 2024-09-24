import asyncio


async def get_data():
    await asyncio.sleep(1)
    return "Some data"


async def main():
    result = await get_data()
    print(result)


asyncio.run(main())
