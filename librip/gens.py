from random import randint


# Генератор вычленения полей из массива словарей
def field(items, *args):
    assert len(args) > 0
    for item in items:
        (len(args) > 1 or item[args[0]] is not None) and \
            (yield {arg: item[arg] for arg in args if item[arg] is not None}
             if len(args) > 1 else item[args[0]])


# Генератор списка случайных чисел
def gen_random(begin, end, num_count):
    for _ in range(num_count):
        yield randint(begin, end)
