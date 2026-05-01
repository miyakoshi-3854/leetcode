"""
239. Sliding Window Maximum

条件
window_legth = len(k)
その時のmax(window)の値を[]にいれて返す

思考
固定幅の尺取り法 (sliding window)
その時その時のmax(window)を返すだけ

rが動くたびwindowの長さをkになるようにlを動かす

window[l:r] をo(n)で取得したいけど、どうやってやるんだろう。
→ index key : 値 value でo(n)取得出来るんじゃね
→→ 貪欲法的に考えて、一番大きい値を記録しておく変数を作るのがいいんじゃね？
→→→ これもだめだ
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            r += 1

        return result
