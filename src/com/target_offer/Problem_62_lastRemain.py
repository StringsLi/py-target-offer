class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        flag = 0
        for i in range(2, n+1):
            flag = (flag + m) % i
        return flag


if __name__ == '__main__':
    n = 5
    m = 3
    obj = Solution()
    print(obj.lastRemaining(n, m))
