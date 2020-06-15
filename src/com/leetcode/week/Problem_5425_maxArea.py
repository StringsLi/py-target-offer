from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def diff(nums: List[int]) -> List[int]:
            res = [0] * (len(nums) - 1)
            for i in range(len(res)):
                res[i] = nums[i + 1] - nums[i]
            return res

        horizontalCuts.append(h)
        horizontalCuts.insert(0, 0)
        verticalCuts.append(w)
        verticalCuts.insert(0, 0)
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        horizontal = diff(horizontalCuts)
        vertical = diff(verticalCuts)

        return int((max(horizontal) * max(vertical)) % (1e9 + 7))


if __name__ == '__main__':
    obj = Solution()
    h = 50
    w = 15
    horizontalCuts = [37, 40, 41, 30, 27, 10, 31]
    verticalCuts = [2, 1, 9, 5, 4, 12, 6, 13, 11]

    res = obj.maxArea(h, w, horizontalCuts, verticalCuts)
    print(res)
