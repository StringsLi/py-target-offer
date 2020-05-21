# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:21:55 2020

@author: lixin
"""

from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sort = sorted(nums)
        return sort[int(len(nums)/2)]

    # most_common(1)代表寻找次数最多的前1个组，[0][0]代表第一个数组的第一个数字。
    def majorityElement2(self, nums: List[int]) -> int:
        import collections
        count = collections.Counter(nums)
        return count.most_common(1)[0][0]



nums = [1,2,10,4,1,4,3]
sort = sorted(nums)
len = int (len(nums)/2)
print(len)
print(sort)
sl = Solution()




