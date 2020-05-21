"""
二叉搜索树有：

结点值:左<根<右
左右子树都是搜索树
后序遍历顺序为：左->右->根

最后一个数为根结点，通过根节点值切割左右子树。
判断左右子树是否二叉搜索树


"""

from typing import List
class Solution:
    def help(self, sequence):
        if len(sequence) <= 1:
            return True
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        for j in range(i, len(sequence) - 1):
            if root > sequence[j]:
                return False
        return self.help(sequence[:i]) and self.help(sequence[i:-1])

    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        return self.help(postorder)




postorder = [1,3,2,6,5]
obj = Solution()

res = obj.verifyPostorder(postorder)
print(res)