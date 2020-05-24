class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        prev, curr = 1, 1
        for _ in range(3, n+1):
            prev, curr = curr, prev+curr
        return curr%(1000000007)

