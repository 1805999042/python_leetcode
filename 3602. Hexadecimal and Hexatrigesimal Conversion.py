# class Solution:
#     def concatHex36(self, n: int) -> str:
#         def to_base(cur: int, base: int) -> str:
#             digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 0..35
#             if cur == 0:
#                 return "0"
#             out = []
#             while cur > 0:
#                 reminder = cur % base          # remainder
#                 quotient = cur // base               # quotient
#                 cur = quotient
#                 out.append(digits[reminder])
#             return "".join(reversed(out))

#         sq = n                                             # n^2
#         cube = n                                          # n^3
#         return to_base(sq, 2) + to_base(cube, 16)
# print(Solution().concatHex36(10)) # "6401A"
# Solution().concatHex36(10) # "1000001C200"

def to_base(cur: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("base must be in [2, 36]")
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if cur == 0:
        return "0"
    out = []
    while cur > 0:
        remainder = cur % base
        quotient = cur // base
        cur = quotient
        out.append(digits[remainder])

    return "".join(reversed(out))
print(to_base(10, 2))  # "1010"
print(to_base(10, 16)) # "A"