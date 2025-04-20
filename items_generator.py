import random


def generate_item_simple(start, end):
    """Генерирует случайный предмет."""
    size = random.randint(start, end)
    return size

def generate_item(start, end):
    """Генерирует случайный предмет."""
    size = random.randint(start, end)
    value = random.randint(start, end)
    return size, value

def generate_item_worst(capacity):
    return capacity // 2 + 1

def generate_worst_case_for_randomized(capacity, threshold):
    """
    Генератор: при каждом вызове выдаёт следующий предмет, который будет отвергнут
    алгоритмом process_item_randomize, т.е random.random() < threshold.
    Возвращает предметы с целыми весами.
    """
    size = 1
    while True:
        if size > capacity:
            size = capacity
        random.seed(size)
        rand = random.random()
        if rand < threshold:
            yield size
        size += 1
