from typing import List
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ret = [0] * num_people
        i = 0
        while candies:
            ret[i % num_people] += min(i+1, candies)
            candies -= min(i+1, candies)
            i += 1
        return ret

candies = 7
num_people = 4
obj = Solution()
res = obj.distributeCandies(candies, num_people)

print(res)