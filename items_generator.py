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
