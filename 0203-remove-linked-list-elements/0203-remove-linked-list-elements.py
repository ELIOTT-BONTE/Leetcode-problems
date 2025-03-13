from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        prev, current = dummy, head

        while current:
            if current.val == val:
                prev.next = current.next  # Skip the node with the target value
            else:
                prev = current  # Move prev forward only if we don’t delete the node
            current = current.next  # Always move current forward
        
        return dummy.next  # Return new head (dummy.next accounts for edge cases)
