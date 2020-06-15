# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:52:37 2020

@author: lixin
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> List[int]:
        if not root:
            return 0
        queue = [root]
        count = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count += 1

        return count


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    obj = Solution()
    res = obj.maxDepth(root)
    print(res)
