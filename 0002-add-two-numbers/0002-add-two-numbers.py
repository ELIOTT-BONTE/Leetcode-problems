# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = l1
        pointer2 = l2
        dummy = ListNode()
        pointer3 = dummy
        remainder = 0

        while pointer1 or pointer2 or remainder:
            val1 = pointer1.val if pointer1 else 0
            val2 = pointer2.val if pointer2 else 0
            res = val1 + val2 + remainder

            remainder = res//10
            res = res%10
            pointer3.next = ListNode(res)
            pointer1 = pointer1.next if pointer1 else None
            pointer2 = pointer2.next if pointer2 else None
            pointer3 = pointer3.next
        return dummy.next