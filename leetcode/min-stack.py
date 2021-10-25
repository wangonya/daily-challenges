class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.insert(0, val)

    def pop(self) -> None:
        del self.stack[0]

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0);
minStack.push(-3);
assert minStack.getMin() == -3
minStack.pop();
assert minStack.top() == 0
assert minStack.getMin() == -2