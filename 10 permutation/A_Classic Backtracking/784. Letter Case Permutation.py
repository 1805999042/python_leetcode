'''
784. Letter Case Permutation
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
'''
from typing import List, Counter


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        cnt = Counter(s)
        res: List[str] = []
        n = len(s)
        keys = list(cnt.keys())  # 固定遍历顺序（可选）
        def dfs(cur_path:list, cur_i) -> None:
            if cur_i == n:
                res.append(''.join(cur_path))
                return
            if s[cur_i].isdigit():
                cur_path.append(s[cur_i])
                dfs(cur_path, cur_i+1)
                cur_path.pop()
            else:
                cur_path.append(s[cur_i].lower())
                dfs(cur_path, cur_i+1)
                cur_path.pop()
                cur_path.append(s[cur_i].upper())
                dfs(cur_path, cur_i+1)
                cur_path.pop()
        dfs([], 0)
        return res
print(Solution().letterCasePermutation("a1b2"))
