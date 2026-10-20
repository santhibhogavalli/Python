import asyncio
import time
from pathlib import Path

import aiohttp


def measure_time(func):
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = await func(*args, **kwargs)

        elapsed_time = time.perf_counter() - start_time

        print(
            f"{func.__name__} took "
            f"{elapsed_time:.4f} seconds"
        )

        return result

    return wrapper


async def download_file(
    session: aiohttp.ClientSession,
    url: str,
    dest_folder: str = "downloads",
) -> str:
    """
    Asynchronously download a file from a URL.
    """

    Path(dest_folder).mkdir(
        exist_ok=True
    )

    filename = url.split("/")[-1] or "downloaded_file"

    dest_path = Path(dest_folder) / filename

    start = time.perf_counter()

    async with session.get(url) as response:

        response.raise_for_status()

        with open(dest_path, "wb") as f:

            async for chunk in response.content.iter_chunked(8192):

                f.write(chunk)

    elapsed = time.perf_counter() - start

    print(
        f"Downloaded: {filename} "
        f"took {elapsed:.4f} seconds"
    )

    return str(dest_path)


@measure_time
async def download_all(urls: list[str]):

    async with aiohttp.ClientSession() as session:

        tasks = [
            download_file(session, url)
            for url in urls
        ]

        results = await asyncio.gather(*tasks)

    return results


async def main():

    urls = [
        "https://testfile.to/dl/100mb",
        "https://testfile.to/dl/10mb",
        "https://testfile.to/dl/1mb",
    ]

    results = await download_all(urls)

    print("\nDownloaded files:")

    for file_path in results:
        print(file_path)


if __name__ == "__main__":

    asyncio.run(main())