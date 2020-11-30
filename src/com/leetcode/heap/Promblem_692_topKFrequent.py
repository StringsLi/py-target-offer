import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for i, w in enumerate(words):
            count[w] = count.get(i, 0) + 1
        return heapq.nsmallest(k, count, lambda i: (-count[i], i))

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        count = {}
        for i, w in enumerate(words):
            count[w] = count.get(i, 0) + 1
        return heapq.nlargest(k, count, lambda i: (count[i], i))


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
obj = Solution()
res2 = obj.topKFrequent2(words, k)
res = obj.topKFrequent2(words, k)

print(res2)
print(res)
