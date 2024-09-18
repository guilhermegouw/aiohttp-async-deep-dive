import asyncio
import time


async def fetch_data(url):
    await asyncio.sleep(2)
    return "Data from {}".format(url)


async def main():
    tasks = []
    urls = [
        "https://example.com",
        "https://example.net",
    ]

    for url in urls:
        tasks.append(fetch_data(url))

    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
