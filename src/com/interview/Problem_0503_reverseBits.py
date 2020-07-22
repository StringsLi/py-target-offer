class Solution:
    def reverseBits(self, num: int) -> int:
        cnt1, cnt2, res = 0, 0, 0
        for _ in range(32) :
            if num & 1 == 1:
                cnt1, cnt2 = cnt1+1, cnt2+1
            else :
                res = max(res, cnt1)
                cnt1, cnt2 = cnt2+1, 0
            num = num >> 1
        return max(res, cnt1)