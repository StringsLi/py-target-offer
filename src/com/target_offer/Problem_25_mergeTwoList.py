"""
双指针，一快一慢，快指针始终领先慢指针k步，当快指针到达链表的末端时，慢指针刚好满足倒数k个位置的链表

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy

        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)

obj = Solution()

res = obj.mergeTwoLists2(head, head1)

while res:
    print(res.val)
    res = res.next
