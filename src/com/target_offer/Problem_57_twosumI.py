# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 18:07:08 2020

@author: lixin
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, item in enumerate(nums):
            if item in dict:
                return [nums[dict[item]],nums[index]]
            else:
                dict[target - item] = index
                
nums = [10,26,30,31,47,60]
target = 40

sl = Solution()
res = sl.twoSum(nums,target)
