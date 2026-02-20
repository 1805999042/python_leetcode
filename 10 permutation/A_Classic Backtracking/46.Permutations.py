from typing import List

#46.Permutations.py
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res: List[List[int]] = []
#         path: List[int] = []
#         used = [False] * len(nums)

#         def backtracking() -> None:
#             if len(path) == len(nums):
#                 res.append(path.copy())
#                 return

#             for i in range(len(nums)):
#                 if used[i]:
#                     continue  # already used
#                 used[i] = True
#                 path.append(nums[i])
#                 backtracking()
#                 path.pop()
#                 used[i] = False

#         backtracking()
#         return res
# print(Solution().permute([1, 2, 3]))


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))   # 添加排列方案
                return
            for i in range(x, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]  # 交换，将 nums[i] 固定在第 x 位
                dfs(x + 1)                           # 开启固定第 x + 1 位元素
                nums[i], nums[x] = nums[x], nums[i]  # 恢复交换
        res = []
        dfs(0)
        return res
print(Solution().permute([1, 2, 3]))