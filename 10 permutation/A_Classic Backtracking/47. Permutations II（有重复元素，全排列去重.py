from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 1) sort first
        res: List[List[int]] = []
        path: List[int] = []
        used = [False] * len(nums)

        def backtracking() -> None:
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue  # already used

                # 2) same-layer dedup: skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtracking()
                path.pop()
                used[i] = False

        backtracking()
        return res

print(Solution().permuteUnique([1, 1, 2]))


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))   # 添加排列方案
                return
            dic = set()
            for i in range(x, len(nums)):
                if nums[i] in dic: continue # 重复，因此剪枝
                dic.add(nums[i])
                nums[i], nums[x] = nums[x], nums[i]  # 交换，将 nums[i] 固定在第 x 位
                dfs(x + 1)                           # 开启固定第 x + 1 位元素
                nums[i], nums[x] = nums[x], nums[i]  # 恢复交换
        res = []
        dfs(0)
        return res