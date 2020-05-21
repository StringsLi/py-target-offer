"""
双指针，一快一慢，快指针始终领先慢指针k步，当快指针到达链表的末端时，慢指针刚好满足倒数k个位置的链表

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head:ListNode, k:int)->ListNode:
        if not head:
            return None
        fast = head
        slow = head

        for _ in range(k):
            if fast:
                fast = fast.next
            else:
                return None
        while fast:
            fast = fast.next
            slow = slow.next
        return slow

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

obj = Solution()

res = obj.getKthFromEnd(head,2)

while res:
    print(res.val)
    res = res.next

