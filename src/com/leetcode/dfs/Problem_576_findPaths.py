from functools import lru_cache

import collections


class Solution:
    @lru_cache(None)
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        MOD = 10 ** 9 + 7
        memo = collections.defaultdict(int)

        def dfs(memo, i, j, k):
            if (i, j, k) not in memo:
                if i < 0 or i >= m or j < 0 or j >= n:
                    memo[(i, j, k)] = 1
                elif k > 0:
                    for x, y in [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]:
                        memo[(i, j, k)] += dfs(memo, x, y, k - 1)
            return memo[(i, j, k)]

        dfs(memo, i, j, N)
        return memo[(i, j, N)] % MOD

    def findPaths2(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1
        if not N:
            return 0
        MOD = 10 ** 9 + 7
        cnt = 0
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            cnt += self.findPaths(m, n, N - 1, i + dx, j + dy)
        return cnt % MOD


obj = Solution()
res = obj.findPaths2(2, 2, 2, 0, 0)
print(res)
