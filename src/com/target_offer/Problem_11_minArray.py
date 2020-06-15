# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:24:10 2020

@author: lixin
"""

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        if n == 0:
            return 0
        for i in range(1, n):
            if numbers[i] < numbers[i - 1]:
                return numbers[i]
        return numbers[0]


nums = [2, 2, 2, 0, 1]
sl = Solution()
res = sl.minArray(nums)
print(res)

# n = len(nums)
# sum_nums = 0
# for i in range(n):
#    print(i)
#    sum_nums += nums[i]
# n*(n-1)/2 - sum_nums
