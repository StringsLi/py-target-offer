class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left: TreeNode, right: TreeNode) -> bool:
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            return helper(left.left, right.right) and helper(right.left, left.right)

        return root == None or helper(root.left, root.right)
