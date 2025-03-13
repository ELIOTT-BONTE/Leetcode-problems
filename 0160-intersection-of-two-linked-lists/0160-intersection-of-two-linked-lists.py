# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        encountered = set()

        current = headA
        while current:
            encountered.add(current)
            current = current.next
        current = headB
        while current:
            if current in encountered:
                return current
            current = current.next
        return None
        