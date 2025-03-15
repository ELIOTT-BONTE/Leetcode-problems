# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        prev = None
        early, late = head, head
        while i < n:
            early = early.next
            i += 1
        
        while early:
            early = early.next
            prev = late
            late = late.next
        
        #delete node at "late" level
        if prev:

            prev.next = late.next

            return head
        else:
            return head.next
