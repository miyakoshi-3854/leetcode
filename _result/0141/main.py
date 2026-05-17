"""
141. Linked List Cycle

条件
与えられたListNodeがループしているのかどうかを調べる

思考



"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        st = set()
        while head:
            if head in st:
                return True
            else:
                st.add(head)
            head = head.next
        return False
