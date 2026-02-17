# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         a = version1.split(".")  # parts of v1
#         b = version2.split(".")  # parts of v2

#         i = 0  # pointer
#         n = max(len(a), len(b))  # total rounds

#         while i < n:
#             x = int(a[i]) if i < len(a) else 0  # current part of v1
#             y = int(b[i]) if i < len(b) else 0  # current part of v2
#             if x > y:
#                 return 1
#             if x < y:
#                 return -1
#             i += 1

#         return 0

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_len, v2_len = len(version1), len(version2)
        v1_point, v2_point = 0, 0
        while v1_point < v1_len or v2_point < v2_len:
            v1_num = 0
            while v1_point < v1_len and version1[v1_point] != '.':
                v1_num = v1_num * 10 + ord(version1[v1_point]) - ord('0')
                v1_point += 1
            v1_point += 1  # 跳过点号
            v2_num = 0
            while v2_point < v2_len and version2[v2_point] != '.':
                v2_num = v2_num * 10 + ord(version2[v2_point]) - ord('0')
                v2_point += 1
            v2_point += 1  # 跳过点号
            if v1_num != v2_num:
                return 1 if v1_num > v2_num else -1
        return 0
Solution().compareVersion("1.01.0", "1.001.0.0.2")# edge: leading zeros ignored, different lengths, v1 < v2
Solution().compareVersion("1.0.2", "1.0.1") # edge: different lengths, v1 > v2
Solution().compareVersion("1.0.0", "1")  # edge: trail zeros ignored