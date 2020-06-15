class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    递归方式
    """

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

        return inorder(root)[k - 1]

    """迭代方式"""

    def kthSmallest2(self, root: TreeNode, k: int) -> int:

        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

sl = Solution()

res = sl.kthSmallest2(root, 1)
print(res)
