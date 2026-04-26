# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        if k == 1:
            return head

        stack = []
        while head:
            next_node = head.next
            head.next = None
            stack.append(head)
            head = next_node

            if len(stack) == k:
                for _ in range(k):
                    tail.next = stack.pop()
                    tail = tail.next
                stack.clear()

        for node in stack:
            tail.next = node
            tail = tail.next

        return dummy.next
