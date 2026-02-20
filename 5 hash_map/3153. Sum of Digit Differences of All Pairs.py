from typing import List  # List


# class Solution:
#     def sumDigitDifferences(self, nums: List[int]) -> int:
#         res = 0
#         n = len(nums) # [13,23,12]
#         while nums[0] > 0:
#             cnt = [0] * 10 # cnt [0, 0, 1, 2, 0, 0, 0, 0, 0, 0]
#             for i in range(n):
#                 cnt[nums[i] % 10] += 1
#                 nums[i] = nums[i] // 10
#             for i in range(10): # cnt
#                 res += (n - cnt[i]) * cnt[i]
#         return res // 2

# Solution().sumDigitDifferences([13,23,12])

class Solution:  # Solution
    def sumDigitDifferences(self, nums: List[int]) -> int:  # nums: [13,23,12]
        res = 0  # res: 0
        digit_cnts = [[0] * 10 for _ in range(10)]  # digit_cnts: [[0,...,0], ..., [0,...,0]]
        for i, num in enumerate(nums):  # i,num: [(0,13), (1,23), (2,12)]
            y_th_digit = 0  # did: 0
            while num > 0:  # num: [13, 23, 12]
                cur_digit = num % 10  # digit: [3, 3, 2]
                res += i - digit_cnts[y_th_digit][cur_digit]  # res: [0, 0, 0, ...]
                digit_cnts[y_th_digit][cur_digit] += 1  # digit_cnts[did][digit]: [0, 1, ...]
                y_th_digit += 1  # did: [0, 1, 2, ...]
                num //= 10  # num: [13,1  23,2 12,1] 
        return res  # res: int
Solution().sumDigitDifferences([13,23,12])