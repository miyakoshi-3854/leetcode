"""
143. Reorder List

条件
ListNodeを指定の条件に並べ替える
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
headを直接書き換える

思考
入れ替えるために、先に全部取得しないといけないな

偶数 → 先頭から取る
奇数 → 末尾から取る
多分この考え方あってるはず

valsから対応する値を取得したら、popするか？
でも先頭をpopはしたくないから、leftpopがいいかな


"""

from collections import deque


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        vals = deque([])

        node = head
        head = head.next
        while head:
            vals.append(head.val)
            head = head.next

        loop = 0
        while vals:
            node.next = ListNode()
            node = node.next
            if loop % 2 == 0:
                node.val = vals.pop()
                loop += 1
            else:
                node.val = vals.popleft()
                loop += 1
