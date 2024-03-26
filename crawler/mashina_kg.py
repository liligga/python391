import asyncio
import httpx
from parsel import Selector
from pprint import pprint


class MashinaKgCrawler:
    MAIN_URL = "https://www.mashina.kg/search/all/?page="
    BASE_URL = "https://www.mashina.kg"

    async def get_page(self, url: str, client: httpx.AsyncClient):
        response = await client.get(url)
        return response

    def get_page_title(self):
        selector = Selector(self.response.text)
        title = selector.css("title::text").get()
        # print(title)

    def get_car_links(self, html):
        selector = Selector(html)
        cars = selector.css("div.list-item a::attr(href)").getall()
        cars = [f"{MashinaKgCrawler.BASE_URL}{car}" for car in cars]
        return cars[:2]
    
    async def get_mashina_kg_data(self):
        async with httpx.AsyncClient() as client:
            tasks = []
            for i in range(1, 11):
                new_task = asyncio.create_task(self.get_page(f"{MashinaKgCrawler.MAIN_URL}{i}", client))
                tasks.append(new_task)
            
            results = await asyncio.gather(*tasks)
            all_car_links = []
            for res in results:
                cars = self.get_car_links(res.text)
                print(cars)
                all_car_links.extend(cars)
            return all_car_links

    def get_data(self):
        self.get_mashina_kg()
        links = self.get_car_links()
        return links
    
# def return_links():
#     return ['https://www.mashina.kg/audi/a6/2021/158956/', 'https://www.mashina.kg/audi/a6/2021/158956/']

if __name__ == "__main__":
    crawler = MashinaKgCrawler()
    # crawler.get_mashina_kg()
    # crawler.get_page_title()
    # cars = crawler.get_car_links()
    # cars = crawler.get_data()
    # pprint(cars)
    asyncio.run(crawler.get_mashina_kg_data())