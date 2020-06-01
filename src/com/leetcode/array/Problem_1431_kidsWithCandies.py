from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [True] * len(candies)
        for i in range(0, len(candies)):
            num = candies[i] + extraCandies
            copy_extra = candies.copy()
            del copy_extra[i]
            if num < max(copy_extra):
                res[i] = False
        return res

    def kidsWithCandies2(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ret = [candy + extraCandies >= maxCandies for candy in candies]
        return ret



if __name__ == '__main__':
    obj = Solution()
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(obj.kidsWithCandies2(candies, extraCandies))