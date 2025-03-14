# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1 = list1
        head2 = list2
        dummy = ListNode()
        res = dummy

        while head1 and head2:
            if head1.val < head2.val:
                res.next = head1
                res = res.next
                head1 = head1.next
            else:
                res.next = head2
                res = res.next
                head2 = head2.next
        if head1:
            res.next = head1
        elif head2:
            res.next = head2
        return dummy.next
