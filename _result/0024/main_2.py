# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while head and head.next:
            first, second = head, head.next
            first.next = second.next
            second.next = first
            tail.next = second
            tail = first
            head = first.next

        if head:
            tail.next = head

        return dummy.next
