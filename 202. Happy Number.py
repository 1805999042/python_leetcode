#Method 1: Use hash sets to detect cycles
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                digit = n % 10          # get last digit
                total_sum += digit * digit  # add square
                n //= 10                # remove last digit
            return total_sum
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1
# Solution().isHappy(19)  # True
Solution().isHappy(116)   # False