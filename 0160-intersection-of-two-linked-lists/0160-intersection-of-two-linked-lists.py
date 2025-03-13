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
            encountered.add(current)  # Store the actual node reference
            current = current.next
        
        current = headB
        while current:
            if current in encountered:  # Check if the node itself (not value) exists in the set
                return current
            current = current.next
        
        return None