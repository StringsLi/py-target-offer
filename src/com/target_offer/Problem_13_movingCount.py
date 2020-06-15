class Solution:
    def digitSum(self, num):
        res = 0
        while num:
            res += num % 10
            num = num // 10
        return res

    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i, j - 1) in vis or (i - 1, j) in vis) and (self.digitSum(i) + self.digitSum(j) <= k):
                    vis.add((i, j))
        return len(vis)
