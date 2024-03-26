import httpx
from time import perf_counter

URL = 'https://www.mashina.kg/search/all/?page'
start = perf_counter()
for i in range(1, 11):
    response = httpx.get(f"{URL}={i}")
    print("Page: ", i, "Status: ", response.status_code)

print("Time: ", perf_counter() - start)