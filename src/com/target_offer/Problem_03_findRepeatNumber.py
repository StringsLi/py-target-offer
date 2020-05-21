# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:21:55 2020

@author: lixin
"""

from collections import Counter
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        stay = set()
        for num in nums:
            if num in stay:
                return num
            else:
                stay.add(num)

    def findRepeatNumberII(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i in count.keys():
            if count[i] > 1:
                return i


nums = [2, 3, 1, 0, 2, 5, 3]
sl = Solution()
res = sl.findRepeatNumber(nums)
res2 = sl.findRepeatNumberII(nums)

print(res)



