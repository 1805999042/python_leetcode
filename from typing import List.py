from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        if n == 0:
            return s
        net = 0  # net > 0 means shift left, net < 0 means shift right  # inline comment
        for direction, amount in shift:
            if direction == 0:
                net += amount  # left shift adds  # inline comment
            else:
                net -= amount  # right shift subtracts  # inline comment

        net %= n  # normalize to [0, n-1]  # inline comment
        return s[net:] + s[:net]  # left shift by net  # inline comment
Solution().stringShift(s = "abc", shift = [[0,1],[1,2]])