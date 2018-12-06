# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, ignore_case=False):
        self.known = set()
        self.items = items
        self.ignore_case = ignore_case

    def __next__(self):
        for item in self.items:
            x = item
            if self.ignore_case and type(x) == str:
                x = x.lower()
            if x not in self.known:
                self.known.add(x)
                return x
        raise StopIteration

    def __iter__(self):
        return self
