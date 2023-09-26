class BubbleSort(Sort):
    """Class that represents a BubbleSort implementation."""

    def _sort(self, items):
        if not isinstance(items, list):
            raise ValueError("It must be a list")
        if not all(isinstance(x, (int, float)) for x in items):
            raise ValueError("All elements in the list must be integers or floats")
        n = len(items)
        for i in range(len(items),0,-1):
          for j in range(i):
            if j+1<len(items) and items[j]>items[j+1]:
              temp=items[j]
              items[j]=items[j+1]
              items[j+1]=temp
        return items

    def _time(self, items):
        import time
        start_time = time.time()
        sorted_items = self._sort(items)
        end_time = time.time()
        self.time = end_time - start_time
        return self.time
