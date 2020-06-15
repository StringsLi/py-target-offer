from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        list = []
        if root is None:
            return list

        def find(root, sum, path):
            sum -= root.val
            if root.left is None and root.right is None and sum == 0:
                list.append(path + [root.val])
            if root.left:
                find(root.left, sum, path + [root.val])
            if root.right:
                find(root.right, sum, path + [root.val])

        find(root, sum, [])
        return list


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sl = Solution()

res = sl.pathSum(root, 12)
print(res)
