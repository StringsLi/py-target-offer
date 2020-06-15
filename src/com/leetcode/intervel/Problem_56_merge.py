from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals or len(intervals) == 0:
            return res
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals):
            left = intervals[i][0]
            right = intervals[i][1]
            while i < len(intervals) - 1 and right >= intervals[i + 1][0]:
                i += 1
                right = max(right, intervals[i][1])
            res.append([left, right])
            i += 1
        return res


intervels = [[1, 3], [8, 10], [15, 18], [2, 6]]

obj = Solution()
res = obj.merge(intervels)

print(res)
