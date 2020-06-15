# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def r_serialize(self, root, str1):
        if not root:
            str1 += "None,"
        else:
            str1 += str(root.val) + ","
            str1 = self.r_serialize(root.left, str1)
            str1 = self.r_serialize(root.right, str1)
        return str1

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.r_serialize(root, "")

    def r_deserialize(self, lst):
        if lst[0] == "None":
            lst.remove(lst[0])
            return None
        else:
            root = TreeNode(int(lst[0]))
            lst.remove(lst[0])
            root.left = self.r_deserialize(lst)
            root.right = self.r_deserialize(lst)

        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        lst = list(data.split(","))
        return self.r_deserialize(lst)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sl = Codec()
res = sl.serialize(root)
print(res)

print(sl.deserialize(res).val)
