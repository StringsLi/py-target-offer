class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head

        occurred = []
        occurred.append(head.val)

        pos = head
        while pos.next:
            cur = pos.next
            if cur.val not in occurred:
                pos = pos.next
                occurred.append(cur.val)
            else:
                pos.next = pos.next.next

        pos.next = None
        return head