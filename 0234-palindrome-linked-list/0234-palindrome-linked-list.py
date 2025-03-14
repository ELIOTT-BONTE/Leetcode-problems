# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        #find middle
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow

        #reverse second part
        prev = None

        while middle:
            nextNode = middle.next
            middle.next = prev
            prev = middle
            middle = nextNode

        #compare second part to first part
        while head and prev:
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next
        
        return True