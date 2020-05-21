from  typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        tmp=[]
        for i in range(1, target):
            max_ = i
            for j in range(i+1, target):
                max_ += j
                if max_ > target:
                    break
                if max_ == target:
                    tmp.append([k for k in range(i, j+1)])
        return tmp

    def findContinuousSequence2(self, target: int) -> List[List[int]]:
        def func(start, end):
            return [i for i in range(start, end + 1)]

        def sum_(start, end):
            # return (end - start + 1) * (end + start) / 2
            return sum(range(start, end+1))

        start = 1
        end = 2
        ans = []
        while start < end:
            if sum_(start, end) < target:
                end += 1
            elif sum_(start, end) > target:
                start += 1
            else:
                ans.append(func(start, end))
                start += 1
        return ans


obj = Solution()

res = obj.findContinuousSequence(15)
res1 = obj.findContinuousSequence2(15)
print(res1)