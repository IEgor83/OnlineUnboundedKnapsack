import random
from time import sleep

from items_generator import generate_item_simple
from online import UnboundedOnlineKnapsack

knapsack = UnboundedOnlineKnapsack(capacity=50, bits=4)

while True:
    item = generate_item_simple(1, 10)
    print('item', item)
    print(knapsack.process_item_randomize(size=item))
    print(knapsack.get_result())
    sleep(3)
