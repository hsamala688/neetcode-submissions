class MinStack:

    def __init__(self):
        
        self._container = []

    def push(self, val: int) -> None:

        self._container.insert(0, val)

    def pop(self) -> None:
        
        if len(self._container) == 0:
            return null

        self._container.pop(0)

    def top(self) -> int:
        
        return self._container[0]

    def getMin(self) -> int:

        min_val = self._container[0]

        for i in range(len(self._container)):
            if min_val > self._container[i]:
                min_val = self._container[i]

        return min_val