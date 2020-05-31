from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)  # 邻接表
        for f, t in tickets:
            d[f] += [t]
        for f in d:
            d[f].sort()
        ans = []
        def dfs(f):
            while d[f]:
                dfs(d[f].pop(0))
            ans.insert(0, f)
        dfs("JFK")
        return ans