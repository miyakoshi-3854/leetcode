"""
567. Permutation in String

条件
s1のアナグラムがs2に存在するか

思考
s1_dictを作る
window_dictを作る

s1_dict == window_dict が True になったら終わり
loopが終了したら False

"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d = defaultdict(int)
        for c in s1:
            s1_d[c] += 1

        window_d = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            if (r - l + 1) > len(s1):
                if s2[l] in s1_d:
                    window_d[s2[l]] -= 1
                l += 1

            if s2[r] in s1_d:
                window_d[s2[r]] += 1

            if s1_d == window_d:
                return True

        return False
