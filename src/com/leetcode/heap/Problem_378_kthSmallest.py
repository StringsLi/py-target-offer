import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = [y for x in matrix for y in x]
        print(lst)
        return heapq.nsmallest(k, lst)[-1]


if __name__ == '__main__':
    obj = Solution()
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ],
    k = 8
    obj.kthSmallest(matrix, k)
