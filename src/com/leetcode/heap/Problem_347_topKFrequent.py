import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), count.get)


nums = [1, 2, 2, 3, 2, 1, 1]
obj = Solution()
res = obj.topKFrequent(nums, 2)
print(res)
