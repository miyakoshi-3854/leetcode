# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(val=None)
        dummy = result
        while list1 is not None or list2 is not None:
            if list1 == None:
                result.next = ListNode(val=list2.val)
                result = result.next
                list2 = list2.next
            elif list2 == None:
                result.next = ListNode(val=list1.val)
                result = result.next
                list1 = list1.next
            elif list1 is not None or list2 is not None:
                if list1.val < list2.val:
                    result.next = ListNode(val=list1.val)
                    result = result.next
                    list1 = list1.next
                else:
                    result.next = ListNode(val=list2.val)
                    result = result.next
                    list2 = list2.next

        return dummy.next
