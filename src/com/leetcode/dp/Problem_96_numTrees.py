
"""
G(n) 代表长度为n序列能构成不同的二叉搜索树的个数
F(i,n):表示以i为根，序列长度为n的不同的二叉搜索树的个数（1 <= i <= n)

G(n) = \sum_{i=1}^{n}F(i,n)

F(i,n) = G(i-1) * G(n-i)

递归公式
G(n) = \sum_{i=1}^{n}G(i-1)(n-i)

实际上，n个不同的数入栈后的出栈的排列总数也是卡特兰数，跟上述二叉搜索树个数的推导其实是一样的，
即每次固定一个出栈的数，即：栈内各个数的排列总数×已出栈的排列总数。
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]