from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumNums = sum(nums)
        sumN = n * (n + 1) // 2
        return sumN - sumNums


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    obj = Solution()
    ress = obj.missingNumber(nums)
    print(ress)
