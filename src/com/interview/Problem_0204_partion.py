from src.com.interview.Problem_0201_removeDuplicateNodes import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p, q = head, head
        while q:
            if q.val < x:
                q.val, p.val = p.val, q.val
                p = p.next
            q = q.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    obj = Solution()

    node = obj.partition(head,2)
    print()
