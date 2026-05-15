"""
206. Reverse Linked List

条件
linked listを逆に入れ替える

思考
linked list全部取り出す
stackに入れておく
popで取り出す
linked list作る

これでいけるか
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        dummy = ListNode()

        while head:
            stack.append(head.val)
            head = head.next

        cur = dummy
        while stack:
            cur.next = ListNode()
            cur = cur.next
            cur.val = stack.pop()

        return dummy.next
