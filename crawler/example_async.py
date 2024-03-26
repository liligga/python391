import asyncio
from time import perf_counter
import httpx

URL = 'https://www.mashina.kg/search/all/?page'

async def get_page(url: str, client: httpx.AsyncClient) -> tuple[int, str, str]:
    response = await client.get(url)
    # print(f"Page: {url} Status: {response.status_code}")
    return response.status_code, url, response.text

async def pack_request_tasks():
    async with httpx.AsyncClient() as client:
        tasks = []
        for i in range(1, 11):
            new_task = asyncio.create_task(get_page(f"{URL}={i}", client))
            tasks.append(new_task)
        
        results = await asyncio.gather(*tasks)
        for status_code, url, _ in results:
            print("Page: ", url, "Status: ", status_code)

if __name__ == '__main__':
    start = perf_counter()
    asyncio.run(pack_request_tasks())
    print("Time: ", perf_counter() - start)