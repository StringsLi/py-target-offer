from src.com.interview.Problem_0201_removeDuplicateNodes import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodeset = set()
        node = head
        while node:
            if node in nodeset:
                return node
            nodeset.add(node)
            node = node.next
        return None

    """
    检测有没有环，使用快慢指针slow和fast（一次走两步）；
    找位置，当找到环之后，slow从head出发，fast从相遇点出发，一次都走一步，再次相遇为环的入口点
    """

    def detectCycle2(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None

        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
