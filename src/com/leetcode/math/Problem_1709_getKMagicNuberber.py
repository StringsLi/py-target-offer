"""
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:

输入: k = 5

输出: 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/get-kth-magic-number-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

这个和ugly Num 很类似

"""


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [1] * k
        u3, u5, u7 = 0, 0, 0
        for i in range(1, k):
            dp[i] = min(dp[u3] * 3, min(dp[u5] * 5, dp[u7] * 7))
            if dp[i] == dp[u3] * 3:
                u3 += 1
            if dp[i] == dp[u5] * 5:
                u5 += 1
            if dp[i] == dp[u7] * 7:
                u7 += 1
        return dp[k - 1]
