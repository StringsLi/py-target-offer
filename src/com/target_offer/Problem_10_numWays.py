class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 2:
            return n
        cur, pre = 2, 1
        for _ in range(3, n+1):
            pre, cur = cur, pre+cur
        return cur % 1000000007

if __name__ == '__main__':
    obj = Solution()
    print(obj.numWays(4))