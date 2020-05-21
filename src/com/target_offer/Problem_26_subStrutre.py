"""
首先要遍历A找出与B根节点一样值的节点R
然后判断树A中以R为根节点的子树是否包含和B一样的结构
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        res = False
        if A and B:
            if A.val == B.val:
                res = self.help(A, B)
            if not res:
                res = self.isSubStructure(A.left, B)
            if not res:
                res = self.isSubStructure(A.right, B)
        return res

    def help(self, A, B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.help(A.left, B.left) and self.help(A.right, B.right)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

root1 = TreeNode(3)
root1.left = TreeNode(9)

sl = Solution()

res = sl.isSubStructure(root,None)
print(res)
