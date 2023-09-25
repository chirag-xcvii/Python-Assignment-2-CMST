from abc import ABC, abstractmethod

class Search(ABC):
    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _search(self, x, y):
        pass

    def get_items(self):
        return self._items

    def _time(self):
        self.time = 0
        return self.time