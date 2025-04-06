import random
from time import sleep


class UnboundedOnlineKnapsack:
    def __init__(self, capacity=1.0):
        self.capacity = capacity
        self.current_fill = 0.0
        self.total_value = 0.0
        self.first_item_seen = False
        self.decisions = []

    def process_item(self, size):
        """
        Обрабатывает поступающий предмет
        size: размер предмета (0 < size <= 1)
        value: ценность предмета (в простой версии равна размеру)
        Возвращает количество взятых копий предмета
        """
        if not self.first_item_seen:

            # Вычисляем, сколько раз можем взять первый предмет
            copies = int(self.capacity / size)
            self.current_fill = copies * size
            self.total_value = copies * size
            self.decisions.append((copies, size))
            self.first_item_seen = True
            return copies
        else:
            # Для всех последующих предметов берем 0 копий
            self.decisions.append((0, size))
            return 0

    def get_result(self):
        """Возвращает текущее заполнение рюкзака и общую ценность"""
        return self.current_fill, self.total_value, self.decisions


def generate_item():
    """Генерирует случайный предмет."""
    size = random.randint(1, 10)  # Генерируем случайный вес, который равен ценности
    return size

generator = generate_item
knapsack = UnboundedOnlineKnapsack(20)

while True:
    item = generator()
    knapsack.process_item(item)
    print(knapsack.get_result())
    sleep(5)
