from src.com.target_offer.Problem_07_rebuildtree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def f(r, s):
            if r:
                s = [i + r.val for i in s] + [r.val]
                return s.count(sum) + f(r.left, s) + f(r.right, s)
            return 0
        return f(root, [])

        def pathSum2(self, root: TreeNode, sum: int) -> int:
            if not root:
                return 0
            return self.path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

        def path(self, root, sum):
            if not root:
                return 0
            res = 0
            if root.val == sum:
                res += 1
            res += self.path(root.left, sum - root.val)
            res += self.path(root.right, sum - root.val)
            return res


if __name__ == '__main__':
    node = TreeNode(5)
    node.left = TreeNode(4)
    node.right = TreeNode(8)
    node.right.left = TreeNode(13)
    node.right.right = TreeNode(4)
    node.right.right.left = TreeNode(5)
    node.right.right.right = TreeNode(1)

    node.left.left = TreeNode(11)
    node.left.left.left = TreeNode(7)
    node.left.left.right = TreeNode(2)

    obj = Solution()
    print(obj.pathSum(root=node,sum=22))
