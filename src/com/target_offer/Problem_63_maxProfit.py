from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        profit = 0
        min_v = prices[0]
        for i in range(1, len(prices)):
            min_v = min(prices[i], min_v)
            profit = max(profit, prices[i] - min_v)
        return profit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    obj = Solution()
    res = obj.maxProfit(prices)
    print(res)