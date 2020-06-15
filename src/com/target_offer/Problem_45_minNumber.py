from typing import List


class cmpSmaller(str):
    def __lt__(self, y):
        return self + y < y + self  # 字符串拼接比较(两两比较)
    # 按由小到大来排列


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        strNum = map(str, nums)
        res = sorted(strNum, key=cmpSmaller)
        return ''.join(res)


obj = Solution()
nums = [1, 2, 3]
res = obj.minNumber(nums)
print(res)
