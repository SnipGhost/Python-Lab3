#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

print(list(Unique(data1)))
print(list(Unique(data2)))

# -----------------------------------------------

data3 = ['a', 'A', 'b', 'B', 'a', 'b']
data4 = ['a', 'b', 'c', 'A', 'b', 'B']

print(list(Unique(data3)))
print(list(Unique(data3, ignore_case=True)))
print(list(Unique(data4)))
print(list(Unique(data4, ignore_case=True)))

# -----------------------------------------------

data5 = ['A', 1, 2, 'a', 2, 2, 'b', 'c', 'B']

print(list(Unique(data5)))
print(list(Unique(data5, ignore_case=True)))
