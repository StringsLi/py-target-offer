# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:19:42 2020

@author: lixin
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        flag = 0
        while queue:
            flag += 1
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if flag % 2 == 0:
                level.reverse()
            res.append(level)

        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sl = Solution()

res = sl.levelOrder(root)
print(res)
