from typing import List
from itertools import accumulate

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        cussum = list(accumulate(shifts[::-1]))[::-1]
        ret = ''
        for i in range(len(shifts)):
            ret += chr((ord(S[i]) + cussum[i] - 97)%26 + 97)
        return ret

S = "abc"
shifts = [3,5,9]
obj = Solution()
res = obj.shiftingLetters(S,shifts)
print(res)