from typing import List
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        gost = 0
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                gost += 1
                continue
            if nums[i + 1] == nums[i]:
                return False
            if (nums[i + 1] - nums[i]) != 1:
                gost -= (nums[i + 1] - nums[i] - 1)
        return gost >= 0

nums = [0,0,0,0,0]

obj = Solution()
ress = obj.isStraight(nums)
print(ress)