from src.com.target_offer.Problem_07_rebuildtree import TreeNode


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:

        res = False
        if t1 and t2:
            if t1.val == t2.val:
                res = self.help(t1, t2)
            if not res:
                res = self.checkSubTree(t1.left, t2)
            if not res:
                res = self.checkSubTree(t1.right, t2)
        return res

    def help(self, A, B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.help(A.left, B.left) and self.help(A.right, B.right)