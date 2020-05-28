from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums == []:
            return []
        max_all = []
        num_nums = len(nums)
        for i in range(num_nums - k + 1):
            max_all.append(max(nums[i:i+k]))
        return max_all


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    obj = Solution()
    print(obj.maxSlidingWindow(nums, k))
