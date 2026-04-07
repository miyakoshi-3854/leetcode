# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            cur = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            cur.next = list1 or list2
            return dummy.next

        if not lists:
            return None

        while len(lists) > 1:
            next_round = []
            for i in range(0, len(lists), 2):
                if i + 1 >= len(lists):
                    next_round.append(lists[i])
                else:
                    next_round.append(mergeTwoLists(lists[i], lists[i + 1]))
            lists = next_round

        return lists[0]