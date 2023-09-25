from abc import ABC, abstractmethod

"""Module with the base implementation of a Sort class."""

class Sort(ABC):
    """Abstract base class for sorting."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _sort(self):
        """Returns the sorted version of the elements contained
        in the `_items` property.
        Returns:
            List: The sorted elements.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self):
        self.time = 0
        return self.time
    
class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""   
    def _sort(self):
        if not isinstance(items, list):
            raise ValueError("It must be a list")     
        items = self.get_items()
        if len(items) <= 1:
            return items

        middle = len(items) // 2
        left = items[:middle]
        right = items[middle:]

        new1 = MergeSort(left)
        new2 = MergeSort(right)

        def merge(left, right):
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result
        return merge(new1._sort(), new2._sort())