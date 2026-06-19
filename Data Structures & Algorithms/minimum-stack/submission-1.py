class MinStack:

    def __init__(self):
        
        self._container = []

    def push(self, val: int) -> None:

        if not self._container:
            self._container.insert(0, (val, val))

        else:
            previous_min = self._container[0][1]
            
            if val < previous_min:
                current_min = val
            else:
                current_min = previous_min
                
            self._container.insert(0, (val, current_min))

    def pop(self) -> None:
        
        if len(self._container) == 0:
            return None

        self._container.pop(0)

    def top(self) -> int:
        
        return self._container[0][0]

    def getMin(self) -> int:

        return self._container[0][1]