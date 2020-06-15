from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return (nums[1] - 1) * (nums[0] - 1)
        nums = sorted(nums)
        res1 = (nums[1] - 1) * (nums[0] - 1)
        res2 = (nums[-1] - 1) * (nums[-2] - 1)
        return max(res1, res2)


obj = Solution()
nums = [-3, -5, 5, 2]
print(obj.maxProduct(nums))
