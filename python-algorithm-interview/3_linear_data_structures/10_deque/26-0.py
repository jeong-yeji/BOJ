

# design-circular-deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = Node(None), Node(None)
        self.k, self.l = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def add(self, node, new):
        self.l += 1
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def delete(self, node):
        self.l -= 1
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.k == self.l:
            return False
        self.add(self.head, Node(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.k == self.l:
            return False
        self.add(self.tail.left, Node(value))
        return True

    def deleteFront(self) -> bool:
        if self.l == 0:
            return False
        self.delete(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.l == 0:
            return False
        self.delete(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.value if self.l else -1

    def getRear(self) -> int:
        return self.tail.left.value if self.l else -1

    def isEmpty(self) -> bool:
        return self.l == 0

    def isFull(self) -> bool:
        return self.l == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
