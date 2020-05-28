# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:15:21 2020

@author: lixin
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.strip().split()
        return " ".join(lst[::-1])
    

if __name__ == '__main__':
    s = "a good   example"
    obj = Solution()
    res = obj.reverseWords(s)
    print(res)