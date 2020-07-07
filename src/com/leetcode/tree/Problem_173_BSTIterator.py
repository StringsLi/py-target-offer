

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        def inorder(root):
            if not root:
                return
            inorder(root.right)
            self.nums.append(root.val)
            inorder(root.left)
        self.nums = []
        inorder(root)


    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.nums.pop()


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.nums else False