#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title':  None, 'price': 9999, 'color': 'white'},
    {'title':  None, 'price': None, 'color': None},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

print(list(field(goods, 'title')))
print(list(field(goods, 'price')))
print(list(field(goods, 'title', 'price')))
print(list(field(goods, 'price', 'title')))

print(list(gen_random(1, 3, 10)))
print(list(gen_random(1, 10, 1)))
print(list(gen_random(1, 10, 2)))
