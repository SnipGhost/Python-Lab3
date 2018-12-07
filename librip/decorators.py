# Здесь необходимо реализовать декоратор, print_result,
#   который принимает на вход функцию, вызывает её, печатает
#   в консоль имя функции, печатает результат и возвращает значение.
# Если функция вернула список (list),
#   то значения должны выводиться в столбик
# Если функция вернула словарь (dict),
#   то ключи и значения должны выводить в столбик через знак равно


def print_result(foo):
    def wrapper(*args, **kwargs):
        res = foo(*args, **kwargs)
        if type(res) == list:
            data = '\n'.join(map(lambda x: str(x), res))
        elif type(res) == dict:
            data = '\n'.join(['{} = {}'.format(k, v) for k, v in res.items()])
        else:
            data = str(res)
        print('Called:', foo.__name__, '\n' + data)
        return res
    return wrapper
