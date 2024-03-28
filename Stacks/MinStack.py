class MinStack:

    def __init__(self):
        self.stack = [0]
        self.minStack = [0]
        self.size = 1
        self.capacity = 0

    def push(self, val: int) -> None:
        if self.capacity == self.size:
            temp = self.stack + [0] * self.size
            minTemp = self.minStack + [0] * self.size
            self.stack = temp
            self.minStack = minTemp
            self.size *= 2
        self.stack[self.capacity] = val
        val = min(val, self.getMin() if self.capacity > 0 else val)
        self.minStack[self.capacity] = val
        self.capacity += 1

    def pop(self) -> None:
        self.stack[self.capacity - 1] = 0
        self.minStack[self.capacity - 1] = 0
        self.capacity -= 1

    def top(self) -> int:
        return self.stack[self.capacity - 1]

    def getMin(self) -> int:
        return self.minStack[self.capacity - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
