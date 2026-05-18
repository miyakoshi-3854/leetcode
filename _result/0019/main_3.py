"""
19. Remove Nth Node From End of List

条件
末尾からn番目のnodeを取り除く

思考
これ解き方覚えている気がする

fast: 先にn回nodeを進む早い方
slow: n回進んだ後の遅い方

fastがNoneにたどり着いたら、
slowも止まる



"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next
