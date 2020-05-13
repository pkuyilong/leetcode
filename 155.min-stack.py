from collections import deque


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = deque()
        self.min_ele = None

    def push(self, x: int) -> None:
        self.stk.append(x)
        if self.min_ele is None:
            self.min_ele = x
        if x < self.min_ele:
            self.min_ele = x

    def pop(self) -> None:
        if len(self.stk):
            ele = self.stk.pop()
            if ele == self.getMin():
                self.min_ele = min(list(self.stk))
        else:
            return None

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_ele



