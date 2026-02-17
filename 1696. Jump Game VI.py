from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)    
        dp = [0] * n  # dp[i] 表示到达位置i时的最大得分
        dp[0] = nums[0]    # 从索引0出发，0的最大得分为其本身
        monotonic_queue = deque()   # 双端队列，初始加入索引0
        monotonic_queue.append(0)
        
        # 从i=1开始枚举
        for i in range(1, n):
            # 弹出队列内不在[i-k, i-1]范围内的索引
            while monotonic_queue[0] + k < i:
                monotonic_queue.popleft()
            # 队首元素即为[i-k, i-1]范围内dp值最大的索引，dp[i] = nums[i] + max(dp[j]), j∈[i-k, i-1]
            dp[i] = nums[i] + dp[monotonic_queue[0]]
            # 将当前dp加入队列，弹出之前比它小的元素
            while monotonic_queue and dp[monotonic_queue[-1]] <= dp[i]:
                monotonic_queue.pop()
            monotonic_queue.append(i)
 
        return dp[n-1]

Solution().maxResult(nums = [1,-1,-2,4,-7,3], k = 2)