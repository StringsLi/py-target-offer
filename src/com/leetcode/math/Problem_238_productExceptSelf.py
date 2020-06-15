from typing import List

"""
基于左侧和右侧和来计算
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1] * len(nums)
        R = [1] * len(nums)

        for i in range(1, len(nums)):
            L[i] = nums[i - 1] * L[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            R[j] = nums[j + 1] * R[j + 1]
        res = [0] * len(nums)
        for i in range(0, len(nums)):
            res[i] = L[i] * R[i]
        return res
