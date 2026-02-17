# def calculate(s: str) -> int:
#     stk = []#store signed numbers
#     num = 0# current number being built from digits
#     sign = '+'# operator before `num` (default '+' for the first number)

#     for i in range(len(s)):
#         cur = s[i]
#         if cur.isdigit():
#             num = num * 10 + int(cur)  # build multi-digit number

#         # if we meet an operator (+/-) OR we are at the end, we "commit" the previous number
#         if cur == '+' or cur == '-' or i == len(s) - 1:
#             if sign == '+':
#                 stk.append(num)      # push as positive
#             elif sign == '-':
#                 stk.append(-num)     # push as negative

#             sign = cur# update operator for the next number
#             num = 0# reset number buffer

#     res = 0
#     while stk:
#         res += stk.pop()            # sum all signed numbers
#     return res
# calculate("10+20-5+3") # 28
# calculate("100-50+25-10") # 65

def calculate(s: str) -> int:
    stk = []
    num = 0
    sign = "+"
    for i in range(len(s)):
        if s[i].isdigit():
            num = 10 * num + int(s[i])
        if s[i] in "+-*/" or i == len(s) - 1:
            if sign == "+":
                stk.append(num)
            elif sign == "-":
                stk.append(-num)
            elif sign == "*":
                stk[-1] *= num
            else:
                # encountering a division sign, the previous number needs to be used for the division operation.
                stk[-1] = int(stk[-1] / num)
            num = 0
            sign = s[i]
    return sum(stk)
calculate(" 3+5*2 / 2 ") # 5
