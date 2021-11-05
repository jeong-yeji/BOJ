# design-circular-queue


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.size = k
        self.f = self.r = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.r] = value
        self.r = (self.r + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.f] = None
        self.f = (self.f + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.f]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.r - 1]

    def isEmpty(self) -> bool:
        return self.f == self.r and self.queue[self.f] is None

    def isFull(self) -> bool:
        return self.f == self.r and self.queue[self.f] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
