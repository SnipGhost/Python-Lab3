# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5

from datetime import datetime


class timer(object):

    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Elapsed time:', (datetime.now() - self.start).total_seconds())
        if exc_val:
            raise
