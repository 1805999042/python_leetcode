class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        s = []
        if (numerator < 0) != (denominator < 0):
            s.append('-')

        numerator = abs(numerator)  # 整数部分
        denominator = abs(denominator)
        integerPart = numerator // denominator
        s.append(str(integerPart))
        s.append('.')

        indexMap = {}       # 小数部分
        remainder = numerator % denominator
        while remainder and remainder not in indexMap:
            indexMap[remainder] = len(s)
            remainder *= 10
            s.append(str(remainder // denominator))
            remainder %= denominator
        if remainder:  # 有循环节
            insertIndex = indexMap[remainder]
            s.insert(insertIndex, '(')
            s.append(')')

        return ''.join(s)

# Solution().fractionToDecimal(1, 2)  # "0.5"
# Solution().fractionToDecimal(2, 1)  # "2"
# Solution().fractionToDecimal(2, 3)  # "0.(6)"
# Solution().fractionToDecimal(1, 6)  # "0.1(6)"
# Solution().fractionToDecimal(1, 7)  # "0.(142857)"
Solution().fractionToDecimal(1, 333)  # "0.(003)"