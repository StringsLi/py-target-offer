from src.com.target_offer.Problem_07_rebuildtree import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        res = None
        cur = root
        while cur:
            if cur.val <= p.val:
                cur = cur.right
            else:
                res = cur
                cur = cur.left
        return res
