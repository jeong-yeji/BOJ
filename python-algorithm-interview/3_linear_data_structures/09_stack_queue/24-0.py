# implement-queue-using-stacks

# 내가 구현한 방식
# 잘못된 풀이
# 큐는 요소를 삽입하고 삭제하는 위치가 다르지만, 스택은 요소를 삽입,삭제하는 위치가 동일함
# => 스택의 연산만을 사용해서 풀려면 2개의 스택 필요
class MyQueue:
    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s.pop(0)

    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        return len(self.s) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
