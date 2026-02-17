from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.L = deque()  # front ... middle
        self.R = deque()  # after middle ... back

    def _rebalance(self):
        # keep: len(L) == len(R) or len(L) == len(R) + 1
        if len(self.L) > len(self.R) + 1:
            self.R.appendleft(self.L.pop())
        elif len(self.L) < len(self.R):
            self.L.append(self.R.popleft())

    def pushFront(self, val: int) -> None:
        self.L.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.L) > len(self.R):     # L is longer -> insert before middle
            self.R.appendleft(self.L.pop())
        self.L.append(val)                # middle ends at L[-1]

    def pushBack(self, val: int) -> None:
        self.R.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.L and not self.R:
            return -1
        x = self.L.popleft() if self.L else self.R.popleft()
        self._rebalance()
        return x

    def popMiddle(self) -> int:
        if not self.L and not self.R:
            return -1
        x = self.L.pop()                  # middle is always L[-1]
        self._rebalance()
        return x

    def popBack(self) -> int:
        if not self.L and not self.R:
            return -1
        x = self.R.pop() if self.R else self.L.pop()
        self._rebalance()
        return x

q = FrontMiddleBackQueue()
q.pushFront(1)     # ✅ pushFront
q.pushBack(2)      # ✅ pushBack
q.pushMiddle(3)    # ✅ pushMiddle
q.pushMiddle(4)    # ✅ pushMiddle again (test even/odd rebalance)
q.popFront()       # ✅ popFront
q.popMiddle()      # ✅ popMiddle
q.popBack()        # ✅ popBack
q.popFront()       # ✅ popFront again (edge: L empty maybe)
q.popMiddle()      # ✅ popMiddle on empty -> -1
q.popBack()        # ✅ popBack on empty -> -1