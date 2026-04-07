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

        if lists == []:
            return None

        while len(lists) > 1:
            current = []
            for i in range(0, len(lists), 2):
                if i + 1 >= len(lists):
                    current.append(lists[i])
                else:
                    current.append(mergeTwoLists(lists[i], lists[i + 1]))
            lists = current

        return lists[0]