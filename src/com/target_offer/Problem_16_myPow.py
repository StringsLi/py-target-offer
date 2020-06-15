class Solution():
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n & 1:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n // 2)


obj = Solution()
res = obj.myPow(2.0, 10)
print(res)
