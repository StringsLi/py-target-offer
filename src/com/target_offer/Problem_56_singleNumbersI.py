# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:21:55 2020

@author: lixin
"""

from collections import Counter
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = list()
        for i in count.keys():
            if count[i] == 1:
                res.append(i)
        return res


nums = [1, 2, 10, 4, 1, 4, 3, 3]
sl = Solution()
res = sl.singleNumbers(nums)
print(res)
