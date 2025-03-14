# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        encountered = set()

        while head:
            if head in encountered:
                return True
            else:
                encountered.add(head)
                head = head.next
        return False