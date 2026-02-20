from collections import Counter
from typing import List

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)
        res: List[List[str]] = []
        path: List[str] = []
        n = len(tiles)
        keys = list(cnt.keys())  # 固定遍历顺序（可选）
        def dfs() -> None:
            if len(path):
                res.append(path.copy())
            for cur in keys:
                if cnt[cur] == 0:
                    continue
                cnt[cur] -= 1
                path.append(cur)
                dfs()
                path.pop()
                cnt[cur] += 1
        dfs()
        return len(res)

print(Solution().numTilePossibilities("AAB"))


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)

        def dfs() -> int:
            total = 0
            for ch in freq:
                if freq[ch] == 0:
                    continue
                # choose ch: this forms a new non-empty sequence
                total += 1  # count the sequence ending with this choice
                freq[ch] -= 1
                total += dfs()  # extend further
                freq[ch] += 1  # backtrack
            return total
        return dfs()

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)
        keys = list(cnt.keys())
        ans = 0
        def dfs() -> None:
            nonlocal ans
            for ch in keys:
                if cnt[ch] == 0:
                    continue
                ans += 1          # 选了 ch，就形成一个新序列
                cnt[ch] -= 1
                dfs()
                cnt[ch] += 1
        dfs()
        return ans
print(Solution().numTilePossibilities("AAB"))
