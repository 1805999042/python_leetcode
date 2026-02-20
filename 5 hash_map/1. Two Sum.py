from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
# Solution().twoSum([2,7,11,15], 26)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums): #[(0, 2), (1, 7), (2, 11), (3, 15)]
            if target - num in m:
                return [i, m[target - num]]
            m[num] = i    
        return [-1, -1]
Solution().twoSum([2,7,11,15], 26)