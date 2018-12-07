from datetime import datetime


# Контекстный менеджер, после выполнения блока выводит время выполнения в сек
class timer(object):

    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Elapsed time:', (datetime.now() - self.start).total_seconds())
        if exc_val:
            raise
