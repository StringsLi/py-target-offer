"""


"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        if dummy.next.val == val:
            return head.next
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            head = head.next
        return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

obj = Solution()

res = obj.deleteNode(head, 4)
