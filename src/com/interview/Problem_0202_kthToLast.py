from src.com.interview.Problem_0201_removeDuplicateNodes import ListNode


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast = head
        slow = head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val
