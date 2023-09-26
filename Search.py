class LinSearch(Search):
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

        # Linear search algorithm
        for item in x:
            if item == y:
                return True

        # If the element is not found, return False
        return False

    def _time(self, x, y):
        import time
        start_time = time.time()
        result = self._search(x, y)
        end_time = time.time()
        self.time = end_time - start_time
        return self.time