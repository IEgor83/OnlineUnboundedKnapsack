from time import sleep

from items_generator import generate_item_simple, generate_item_worst, generate_worst_case_for_randomized
from ofline import UnboundedOfflineKnapsack
from online import UnboundedOnlineKnapsack

online_knapsack_first = UnboundedOnlineKnapsack(capacity=50, bits=4)
online_knapsack_randomized = UnboundedOnlineKnapsack(capacity=50, bits=4)
threshold = online_knapsack_randomized.threshold

offline_knapsack = UnboundedOfflineKnapsack(capacity=50)
offline_knapsack_for_randomized = UnboundedOfflineKnapsack(capacity=50)

gen = generate_worst_case_for_randomized(capacity=50, threshold=threshold)

items_1 = [generate_item_worst(50)]
items_2 = [next(gen)]
print('item', items_1[0])
print('item_for_randomized', items_2[0])

online_knapsack_first.process_item_first_simple(size=items_1[0])
online_knapsack_randomized.process_item_randomize(size=items_2[0])

print('offline', offline_knapsack.unbounded_knapsack_simple(items_1))
print('offline randomized', offline_knapsack_for_randomized.unbounded_knapsack_simple(items_2))
print('online', online_knapsack_first.get_result()[1])
print('online randomized', online_knapsack_randomized.get_result()[1])
print()

while True:
    item = generate_item_simple(1, 50)
    item_for_randomized = next(gen)

    items_1.append(item)
    items_2.append(item_for_randomized)

    print('item', item)
    print('item_for_randomized', item_for_randomized)

    online_knapsack_first.process_item_first_simple(size=item)
    online_knapsack_randomized.process_item_randomize(size=item_for_randomized)

    print('offline', offline_knapsack.unbounded_knapsack_simple(items_1))
    print('offline randomized', offline_knapsack_for_randomized.unbounded_knapsack_simple(items_2))
    print('online', online_knapsack_first.get_result()[1])
    print('online randomized', online_knapsack_randomized.get_result()[1])
    print()
    sleep(3)
