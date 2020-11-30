from src.com.interview.Problem_0201_removeDuplicateNodes import ListNode

"""
利用双指针同时移动，在到尾部的时候就交换位置.
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
