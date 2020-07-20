from src.com.target_offer.Problem_07_rebuildtree import TreeNode

"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True

"""

class Solution:
    def findTarget(self, root: TreeNode, target: int) -> bool:

        def dfs(root):
            if not root:
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)

        numbers = dfs(root)
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return True
            elif sum > target:
                right -= 1
            else:
                left += 1

        return False