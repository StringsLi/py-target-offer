# Definition for singly-linked list.
"""
们可以使用两个指针而不是一个指针。第一个指针从列表的开头向前移动 n+1n+1 步，
而第二个指针将从列表的开头出发。现在，这两个指针被 nn 个结点分开。我们通过同时移动两个指针向前来保持这个恒定的间隔，
直到第一个指针到达最后一个结点。此时第二个指针将指向从最后一个结点数起的第 nn 个结点。
我们重新链接第二个指针所引用的结点的 next 指针指向该结点的下下个结点。


"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = ListNode(-1)
        res.next = head
        slow = res
        fast = res

        while n > 0:
            fast = fast.next
            n -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return res.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

obj = Solution()

res = obj.removeNthFromEnd(head,2)