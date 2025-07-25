
class MyStack:

    def __init__(self):
        self.q = deque([])

    def push(self, x: int) -> None:
        self.q.append(x)
        self.q.rotate(len(self.q))

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return self.q == deque([])


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()