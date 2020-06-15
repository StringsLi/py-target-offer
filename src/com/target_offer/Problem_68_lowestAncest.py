def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentVal = root.val
        pVal = p.val
        qVal = q.val

        if pVal < parentVal and qVal < parentVal:
            return self.lowestCommonAncestor(root.left, p, q)
        elif pVal > parentVal and qVal > parentVal:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
