from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        max_number = 10 ** n
        res = [1 for _ in range(max_number - 1)]
        for i in range(1, max_number):
            res[i - 1] = i
        return res
