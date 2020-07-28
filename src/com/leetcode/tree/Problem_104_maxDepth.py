from src.com.target_offer.Problem_07_rebuildtree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if not root else max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1