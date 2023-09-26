class BinSearch(Search):
    def _search(self, x, y):
        # Check if x is a list
        if not isinstance(x, list):
            raise ValueError("x must be a list")

        # Check if y is a number (integer or float)
        if not isinstance(y, (int, float)):
            raise ValueError("y must be a number")

        # Check if all elements in the list x are either integers or floats
        if not all(isinstance(i, (int, float)) for i in x):
            raise ValueError("All elements in the list must be integers or floats")

        # Initialize the left and right pointers
        r = len(x) - 1
        l = 0

        # Binary search algorithm
        while l <= r:
            mid = (l + r) // 2
            if x[mid] == y:
                return True
            elif y > x[mid]:
                l = mid + 1
            else:
                r = mid - 1

        # If the element is not found, return False
        return False

def _time(self, x, y):
    import time
    start_time = time.time()
    result = self._search(x, y)
    end_time = time.time()
    self.time = end_time - start_time
    return self.time
