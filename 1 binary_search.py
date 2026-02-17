from typing import List

def bs_find_any(nums: List[int], target: int) -> int:
    if not nums or target < nums[0] or target > nums[-1]:
        return -1

    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1
# print(bs_find_any([1,2,3,4,5,6,7,8,9,10], 9))      # 2


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        return l

# Solution().searchInsert([1,3,5,6], 2) # 1

# def bs_left_bound(nums: List[int], target: int) -> int:
#     if not nums or target < nums[0] or target > nums[-1]:
#         return -1
#     l, r = 0, len(nums) - 1
#     while l <= r:
#         m = l + (r - l) // 2
#         if nums[m] < target:
#             l = m + 1
#         else:
#             r = m - 1   # nums[m] >= target，往左逼
#     if l < len(nums) and nums[l] == target: # 退出时：r < l。l 是第一个 >= target 的位置
#         return l
#     return -1
def left_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    # 搜索区间为 [left, right]
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            # 搜索区间变为 [mid+1, right]
            left = mid + 1
        elif nums[mid] > target:
            # 搜索区间变为 [left, mid-1]
            right = mid - 1
        elif nums[mid] == target:
            # 收缩右侧边界
            right = mid - 1
    return left
left_bound([1,2,3,3,3,3,3,8,9], 3)  # 2
