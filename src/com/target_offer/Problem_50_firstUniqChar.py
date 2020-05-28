# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:05:49 2020

@author: lixin
"""

import collections

class Solution:
    def firstUniqChar(self, s: str) -> str:
        count = collections.Counter(s)
        for char in s:
            if count[char] == 1:
                return char
        return ""
    
    def freq(self, s):
        map = {}
        for i in range(len(s)):
            map[s[i]] = map.get(s[i], 0) + 1
        return map

    
s = "abaccdeff"
obj = Solution()
res = obj.firstUniqChar(s)
print(res)
