from typing import List
import math


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        mid = int(math.sqrt(num)) + 1
        while mid >= 1:
            if (num + 1) % mid == 0:
                return [mid, int((num + 1) / mid)]
            if (num + 2) % mid == 0:
                return [mid, int((num + 2) / mid)]
            mid -= 1
        return []


if __name__ == '__main__':
    num = 14
    obj = Solution()
    print(obj.closestDivisors(num))
