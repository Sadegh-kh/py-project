import asyncio
import time
from tracemalloc import start


async def load_blog():
    print("loading blog")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("blog loaded")


async def get_data_from_database():
    print("loading data")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("data loaded")


async def main():
    start_time = time.time()
    # task1 = asyncio.create_task(load_blog())
    # task2 = asyncio.create_task(get_data_from_database())
    # await asyncio.wait([task1, task2])
    # await asyncio.gather(task1, task2)
    await asyncio.gather(load_blog(), get_data_from_database())

    end_time = time.time()

    print(end_time - start_time)


if __name__ == "__main__":
    asyncio.run(main())
