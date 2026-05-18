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


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. 中間ノードを探す（slow/fast pointer）
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 後半を逆順にする
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. 前半と逆順後半を交互に繋ぐ
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
