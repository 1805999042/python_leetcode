from typing import List

def permutations(nums: List[int]) -> List[List[int]]:
    nums.sort()  # 如果题目可能有重复：先排序；没有重复也不影响正确性（只影响耗时一点点）
    res: List[List[int]] = []
    path: List[int] = []
    used = [False] * len(nums)

    def dfs() -> None:
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            '''
            # 剪枝1：同层去重（47 的核心）
            # 含义：同一层里，遇到重复值，只让“最左边那个没被用过的”来开枝
            '''
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            # 剪枝2：放置前校验（通用条件剪枝）
            # 例：如果你有规则 constraint_ok(path, nums[i])，不满足就跳过
            # if not constraint_ok(path, nums[i]):
            #     continue
            used[i] = True
            path.append(nums[i])
            # 剪枝3：提前结束（上界/下界剪枝）
            # 例：如果剩余怎么都不可能满足目标，就 return（需要你写 bound 函数）
            # if not bound_ok(path, used):
            #     path.pop(); used[i]=False; continue
            dfs()
            path.pop()
            used[i] = False
    dfs()
    return res



from typing import List
def permutations_swap(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res: List[List[int]] = []
    n = len(nums)
    def dfs(first: int) -> None:
        if first == n:
            res.append(nums.copy())
            return
        seen = set()  # 剪枝：同层去重（swap版最常用）
        for i in range(first, n):
            if nums[i] in seen:
                continue
            seen.add(nums[i])

            nums[first], nums[i] = nums[i], nums[first]
            dfs(first + 1)
            nums[first], nums[i] = nums[i], nums[first]
    dfs(0)
    return res

'''
4) 更强剪枝：用“计数表”替代 used（更快更稳）

适合：重复特别多（比如 “aabbbbbcc”），会比 used+sort 更爽。
思路：每次从 count 里选一个还剩的字符/数字。
'''
from collections import Counter
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        res: List[List[int]] = []
        path: List[int] = []
        n = len(nums)
        keys = list(cnt.keys())  # 固定遍历顺序（可选）

        def dfs() -> None:
            if len(path) == n:
                res.append(path.copy())
                return
            for x in keys:
                if cnt[x] == 0:
                    continue
                cnt[x] -= 1
                path.append(x)
                dfs()
                path.pop()
                cnt[x] += 1
        dfs()
        return res
