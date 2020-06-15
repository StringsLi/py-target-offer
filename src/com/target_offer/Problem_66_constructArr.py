from typing import List
from functools import reduce


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        res = [0] * len(a)
        for i in range(len(a)):
            tmp = a[:i] + a[i + 1:]
            res[i] = reduce(lambda x, y: x * y, list(tmp))
        return res

    def constructArr2(self, a: List[int]) -> List[int]:
        l, r = [1], [1]
        for i in range(len(a)):
            l.append(l[-1] * a[i])
            r.append(r[-1] * a[~i])
        return [l[i] * r[~(i + 1)] for i in range(len(a))]


a = [1, 2, 3, 4, 5]
# a.remove(1)
# print(a)
obj = Solution()
res = obj.constructArr2(a)
print(res)
