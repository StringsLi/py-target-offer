from src.com.target_offer.Problem_07_rebuildtree import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)

        res = dfs(root)

        return res == sorted(set(res))
