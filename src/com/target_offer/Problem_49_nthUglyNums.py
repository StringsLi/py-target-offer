class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        u2,u3,u5 = 0, 0, 0
        for i in range(1,n):
            dp[i] = min(dp[u2]*2,min(dp[u3]*3,dp[u5]*5))
            if dp[i] == dp[u2] * 2:
                u2 += 1
            if dp[i] == dp[u3] * 3:
                u3 += 1
            if dp[i] == dp[u5] * 5:
                u5 += 1
        return dp[n-1]