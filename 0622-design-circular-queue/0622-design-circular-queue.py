class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.k = k
        self.frontIdx = 0
        self.rearIdx = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rearIdx = (self.rearIdx + 1) % self.k
        self.queue[self.rearIdx] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # self.queue[self.frontIdx] = 0
        self.frontIdx = (self.frontIdx + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.frontIdx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rearIdx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()