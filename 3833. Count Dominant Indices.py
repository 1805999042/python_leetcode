from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        preSum = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        res = 0
        for i in range(0, len(nums)-1):
            if nums[i] > (preSum[len(nums)] -preSum[i+1])//(len(nums)-(i+1)):
                res+=1
        return res
print(Solution().dominantIndices(nums = [58,89]))

x = 100
for i in range(10):
    x = (x>>1) |1
    print(x)