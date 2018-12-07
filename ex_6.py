#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique


if len(sys.argv) != 2:
    raise ValueError('No filename argument')

with open(sys.argv[1]) as f:
    data = json.load(f)


# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов


@print_result
def f1(arg):
    return sorted(unique(field(arg, 'job-name'), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: 1 if 'программист' in x else 0, arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    s = gen_random(100000, 200000, len(arg))
    return list(map(lambda x: '{}, зарплата {} руб.'.format(*x), zip(arg, s)))


with timer():
    f4(f3(f2(f1(data))))
