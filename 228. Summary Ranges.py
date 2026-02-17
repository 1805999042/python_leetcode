from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        l = []

        def flush():
            if len(l) == 1:
                res.append(str(l[0]))
            else:
                res.append(f"{l[0]}->{l[-1]}")

        for x in nums:
            if not l or x == l[-1] + 1:
                l.append(x)
            else:
                flush()
                l = [x]
        if l:
            flush()
        return res


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res

        start = nums[0]                  # start of current range
        prev = nums[0]                   # last number in current range

        for x in nums[1:]:
            if x == prev + 1:            # still continuous
                prev = x
            else:                        # range ends, flush it
                if start == prev:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{prev}")
                start = prev = x         # start new range

        # flush last range
        if start == prev:
            res.append(str(start))
        else:
            res.append(f"{start}->{prev}")

        return res
