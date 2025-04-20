import random


class UnboundedOnlineKnapsack:
    def __init__(self, capacity=10, bits=4):
        self.capacity = capacity
        self.current_fill = 0
        self.total_value = 0
        self.first_item_seen = False
        self.decisions = []

        # Параметры для случайных битов
        self.bits = bits
        self.threshold = self._generate_threshold(bits)
        self.has_selected_item = False

    @staticmethod
    def _generate_threshold(bits):
        """
        Генерируем случайный порог на основе случайных битов.
        Чем больше битов, тем лучше разрешение.
        """
        max_value = (1 << bits) - 1
        random_bits = random.randint(0, max_value)
        threshold = 0.5 + (random_bits / max_value) * 0.5
        return threshold

    def _process_item(self, size, value=None):

        if value is None:
            value = size

        if not self.first_item_seen:
            copies = self.capacity // size
            self.current_fill = copies * size
            self.total_value = copies * value
            self.decisions.append((copies, size))
            self.first_item_seen = True
            return copies
        else:
            self.decisions.append((0, size))
            return 0

    def process_item_first_simple(self, size):
        """
        Обрабатывает поступающий предмет
        size: размер предмета
        возвращает количество взятых копий предмета
        """
        return self._process_item(size)

    def process_item_first(self, size, value):
        """
        Обрабатывает поступающий предмет
        size: размер предмета
        value: ценность предмета
        возвращает количество взятых копий предмета
        """
        return self._process_item(size, value)

    def process_item_randomize(self, size, value=None):
        """
        Основной алгоритм обработки предмета
        size: размер предмета
        value: ценность предмета
        """
        if value is None:
            value = size

        if self.current_fill >= self.capacity:
            self.decisions.append((0, size))
            return 0

        random.seed(size)
        random_number = random.random()

        if not self.has_selected_item:
            if random_number >= self.threshold:
                copies = (self.capacity - self.current_fill) // size
                self.current_fill += copies * size
                self.total_value += copies * value
                self.decisions.append((copies, size))
                self.has_selected_item = True
                return copies
            else:
                self.decisions.append((0, size))
                return 0
        else:
            potential_copies = (self.capacity - self.current_fill) // size
            if potential_copies > 0:
                self.current_fill += potential_copies * size
                self.total_value += potential_copies * value
                self.decisions.append((potential_copies, size))
                return potential_copies
            else:
                self.decisions.append((0, size))
                return 0

    def clear(self):
        self.current_fill = 0
        self.total_value = 0
        self.first_item_seen = False
        self.decisions = []

    def get_result(self):
        """Возвращает текущее заполнение рюкзака и общую ценность"""
        return self.current_fill, self.total_value, self.decisions
