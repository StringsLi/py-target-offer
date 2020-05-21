from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack

pushed = [1,2,3,4,5]
popped = [4,5,3,1,2]

pushed.pop()

print(pushed)

obj = Solution()
# print(obj.validateStackSequences(pushed,popped))