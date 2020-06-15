from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]


grid = [
    [1, 2, 5],
    [3, 2, 1]
]

obj = Solution()
res = obj.maxValue(grid)
print(res)
