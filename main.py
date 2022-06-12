import logging
from init_logging import init_logging


def double(number: int) -> int:
    logging.info(number)
    return number ** 2


def calculate(items: list[int]):
    return list(map(double, items))


def main():
    start = 100000
    items = list(range(start, start + 200000))
    calculate(items)
    print()


if __name__ == "__main__":
    init_logging()
    main()
