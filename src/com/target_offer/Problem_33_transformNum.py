class Solution:
    def translateNum(self, num: int) -> int:
        cnt = 0
        def helper(s):
            nonlocal cnt
            if not s:
                cnt += 1
                return
            helper(s[1:])
            if len(s) > 1:
                if '09' < s[:2] < '26':
                    helper(s[2:])

        helper(str(num))
        return cnt

    def numDecodings(self,s: str) -> int:
        strNums = s
        size = len(strNums)
        dp = [1] + [0] * size
        for i in range(1, size + 1):
            if strNums[i - 1] >= '1' and strNums[i - 1] <= '9':
                dp[i] += dp[i - 1]

            if i > 1:
                a = int(strNums[i - 2]) * 10 + int(strNums[i - 1])
                if a <= 26 and a >= 10:
                    dp[i] += dp[i - 2]
        return dp[size]


num = "226"
obj = Solution()

res = obj.numDecodings(num)
print(res)