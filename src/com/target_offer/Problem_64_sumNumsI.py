
class Solution:
    def sumNums(self, n: int) -> int:
        def dfs(n):
            return n and n + dfs(n - 1)
        return dfs(n)


if __name__ == '__main__':
    obj = Solution()
    print(obj.sumNums(10))
