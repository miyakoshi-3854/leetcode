"""
21. Merge Two Sorted Lists

条件
二つのlinked listをmergeする

思考
whileで、list1 or list2 で回すのがいいかな

linked listの中身は昇順に並んでいるから、
topを見ればどっちをつなげるべきかわかる

"""


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()

        cur = dummy
        while list1 or list2:
            cur.next = ListNode()
            cur = cur.next

            if not list1:
                cur.val = list2.val
                list2 = list2.next
                continue
            elif not list2:
                cur.val = list1.val
                list1 = list1.next
                continue
            elif list1.val <= list2.val:
                cur.val = list1.val
                list1 = list1.next
            else:
                cur.val = list2.val
                list2 = list2.next

        return dummy.next
