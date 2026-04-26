# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        if not head or not head.next:
            return head

        while head.next:
            if not head.next.next:
                cur.next = ListNode(head.next.val)
                cur.next.next = ListNode(head.val)
                head = head.next.next
                cur = cur.next
                break
            else:
                cur.next = ListNode(head.next.val)
                cur.next.next = ListNode(head.val)
                head = head.next.next
                cur = cur.next.next

        if head:
            cur.next = ListNode(head.val)

        return dummy.next
