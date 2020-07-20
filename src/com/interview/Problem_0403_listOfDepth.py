
from typing import List
from src.com.interview.Problem_0201_removeDuplicateNodes import ListNode
from src.com.target_offer.Problem_07_rebuildtree import TreeNode


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []
        result = []
        queue = [tree]
        while queue:
            queue_len = len(queue)
            p = None
            q = None
            head = None
            for _ in range(queue_len):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                if q is None:
                    q = ListNode(node.val)
                    head = q
                else:
                    p = ListNode(node.val)
                    q.next = p
                    q = p
            result.append(head)
        return result