import asyncio
import logging
import multiprocessing

from init_logging import init_logging
# import multiprocessing
import concurrent.futures
import threading

# multiprocessing.Queue()
# lock = multiprocessing.Lock()
# with lock:
#     ...
multiprocessing.Semaphore()


def double(number: int) -> int:
    logging.info(number)
    return number ** 2


async def double_async(number: int) -> int:
    logging.info(f"start {number}")
    await asyncio.sleep(1)
    logging.info(f"after wait {number}")
    return number ** 2


def calculate_sync(items: list[int]) -> list[int]:
    return list(map(double, items))


def calculate_process(items: list[int]) -> list[int]:
    with concurrent.futures.ProcessPoolExecutor() as worker:
        results = worker.map(
            double,
            items,
        )
        # worker.submit(double, args=(items[0],))
        futures = [
            worker.submit(double, (number,)) for number in items
        ]
        items = concurrent.futures.as_completed(futures)
    return items


def calculate_tread(items: list[int]) -> list[int]:
    with concurrent.futures.ThreadPoolExecutor() as worker:
        results = worker.map(
            double,
            items,
        )
        # worker.submit(double, args=(items[0],))
        futures = [
            worker.submit(double, (number,)) for number in items
        ]
        items = []
        for future in concurrent.futures.as_completed(futures):
            items.append(future.result())

    return items


async def calculate_async(items: list[int]) -> list[int]:
    result = await double_async(number=22)
    await asyncio.gather(*[
        double_async(number) for number in items
    ])


def main():
    start = 100000
    items = list(range(start, start + 200000))
    asyncio.run(calculate_async(items=items))
    # calculate_sync(items=items)
    # calculate_process(items=items)
    # calculate_tread(items=items)
    # thread = threading.Thread(target=double, args=(10, ), daemon=True)
    # thread.start()
    # logging.info('wait')
    # thread.join()
    # logging.info('finish')
    # thread.
    # print()


if __name__ == "__main__":
    init_logging()
    main()
