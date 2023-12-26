import asyncio

from app.services.meal_services import insert_food, get_food
from app.settings import async_session_maker
from app.tables import Food

async def main():
    async with async_session_maker() as session:
        food = set()
        food.add('salo')

        res = await get_food(session, food)
        print(res.first().tuple()[0].name)




if __name__ == "__main__":
    
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

