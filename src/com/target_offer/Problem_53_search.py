from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                i, j = mid, mid
                while i >= 0 and nums[i] == target:
                    i -= 1
                while j <= len(nums) - 1 and nums[j] == target:
                    j += 1
                # j - 1 - (i + 1) + 1
                return j - i - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return 0

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                i, j = mid, mid
                while i >= 0 and nums[i] == target:
                    i -= 1
                while j <= len(nums) - 1 and nums[j] == target:
                    j += 1
                return [i+1, j-1]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [-1, -1]


nums = [5,7,7,8,8,10]

obj = Solution()

res = obj.searchRange(nums, 8)
print(res)