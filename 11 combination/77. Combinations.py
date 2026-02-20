'''
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
'''

from typing import List


# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res: List[List[int]] = []
#         path: List[int] = []
#         def dfs(start: int) -> None:
#             if len(path) == k:
#                 res.append(path[:])
#                 return
#             for i in range(start, n + 1):
#                 path.append(i)
#                 dfs(i + 1)
#                 path.pop()
#         dfs(1)
#         return res
# print(Solution().combine(4, 2))


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res: List[List[int]] = []
        path: List[int] = []
        def dfs(start: int) -> None:
            if len(path) == k:
                res.append(path[:])
                return
            # pruning: remaining numbers count must be enough to fill to k
            need = k - len(path) 
            for i in range(start, n + 1):
                remain = n - i + 1 
                if remain < need:
                    break
                path.append(i)
                dfs(i + 1)
                path.pop()
        dfs(1)
        return res
print(Solution().combine(4, 2))
