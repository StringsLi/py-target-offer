class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return not root or self.helper(root.left, root.right)

    def helper(self, left: TreeNode, right: TreeNode) -> bool:
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)

    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False

        return (left.val == right.val) and self.isMirror(left.right,right.left) and self.isMirror(left.left,right.right)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root1 = TreeNode(3)
root1.left = TreeNode(20)
root1.right = TreeNode(9)

sl = Solution()

res = sl.isSymmetric(root)
print(res)
