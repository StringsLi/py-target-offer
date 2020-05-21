from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.depth(root) != -1:
            return True
        else:
            return False

    def depth(self,root:TreeNode) -> int:
        if not root:
            return 0
        left = self.depth(root.left)
        if left == -1:
            return -1
        right = self.depth(root.right)
        if right == -1:
            return -1

        if abs(left - right) <= 1:
            return max(left, right) + 1
        else:
            return -1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sl = Solution()

res = sl.isBalanced(root)
print(res)
