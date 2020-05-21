class Solution(object):
    def countDigitOne(self, n):
        res = 0
        i = 1  # 个位开始
        while n // i != 0:
            high = n//(i*10) # 高位数
            current = (n//i) % 10  # 第i位数
            low = n - (n//i) * i  # 低位数
            if current == 0:
                res += high * i
            elif current == 1:
                res += high * i + low + 1
            else:
                res += (high+1) * i
            i *= 10
        return res

obj = Solution()
res = obj.countDigitOne(12)
print(res)
