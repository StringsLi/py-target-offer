from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = 0
        mx = A[0] + 0
        for j in range(1, len(A)):
            ans = max(ans, mx + A[j] - j)
            mx = max(mx, A[j] + j)

        return ans


if __name__ == '__main__':
    A = [8, 1, 5, 2, 6]
    obj = Solution()
    print(obj.maxScoreSightseeingPair(A))
