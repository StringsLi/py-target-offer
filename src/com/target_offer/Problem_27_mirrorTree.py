from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return root
        queue = [root]
        while queue:
            current = queue.pop(0)
            tmp = current.left
            current.left = current.right
            current.right = tmp

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sl = Solution()

res = sl.mirrorTree(root)
print(res)
