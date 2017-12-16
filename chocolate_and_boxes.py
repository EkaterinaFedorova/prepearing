# Alice has N boxes, and each box has certain non zero number of chocolates. These boxes are numbered from 1 to N.
#
# Alice is planning to go to wonderland. She wants to carry exactly K number of chocolates and
#  she can carry only 2 boxes.
# So she wants to know the number of ways in which she can select 2 boxes such that total number of
#  chocolates in them is K.
import sys
import numpy as np
from itertools import combinations

with open('chocolate_and_boxes.txt', 'r') as f:
    cases_count = int(f.readline().rstrip('\n'))
    box_count = []
    box_items = []
    chocolate_count = []

    for num in range(cases_count):
        box_count.append(int(f.readline().rstrip('\n')))
        box_items.append(list(map(int, f.readline().split())))
        chocolate_count.append(int(f.readline().rstrip('\n')))

for num in range(cases_count):
    taken = set()
    cases = 0
    for i, chocolates in enumerate(box_items[num]):
        if i in taken:
            continue
        expected = chocolate_count[num] - chocolates

        suitable = {item for item, val in enumerate(box_items[num]) if val == expected}
        suitable = (suitable | {i}) - taken
        result = len(list(combinations(suitable, 2)))
        if result:
            cases += result
            taken = taken | suitable

    print(cases)

# if __name__ == "__main__":
