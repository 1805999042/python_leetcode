from collections import deque
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(range(len(tickets)))  # 队列里放人的 index
        time = 0

        while True:
            i = q.popleft()             # 当前轮到 i
            tickets[i] -= 1             # 买 1 张
            time += 1                   # 用时 +1

            if i == k and tickets[i] == 0:
                return time             # k 买完了就结束

            if tickets[i] > 0:
                q.append(i)             # 还没买完，回到队尾

Solution().timeRequiredToBuy(tickets = [2,3,2], k = 2)