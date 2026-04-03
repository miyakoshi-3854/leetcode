# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = []

        current = head
        while current != None:
            result.append(current.val)
            current = current.next

        result.pop(- n)

        # create ListNode
        node = None
        for val in reversed(result):
            node = ListNode(val, node)

        return node