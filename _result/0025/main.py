# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        reverse = dummy

        if k == 1:
            return head

        stack = []
        while head:
            memory = head.next
            head.next = None
            stack.append(head)
            head = memory

            if len(stack) == k:
                for _ in range(k):
                    reverse.next = stack.pop()
                    reverse = reverse.next
                stack = []

        if stack:
            for _ in range(len(stack)):
                reverse.next = stack.pop(0)
                reverse = reverse.next

        return dummy.next
