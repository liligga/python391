from aiogram import Router, F, types
from crawler.mashina_kg import MashinaKgCrawler
from pprint import pprint


mashina_router = Router()

@mashina_router.callback_query(F.data == "parse_cars")
async def parse_cars(callback: types.CallbackQuery):
    crawler = MashinaKgCrawler()
    links = await crawler.get_mashina_kg_data()
    pprint(links)
    # links = return_links()
    # for link in links:
    #     await callback.message.answer(link)