"""
981. Time Based Key-Value Store

条件
setとgetを自作する

思考
これに二分探索使うのってどういうこと？

set → key ごとに (timestamp, value) をリストに追加
get → そのリストに対して二分探索で「timestamp以下で最大」を探す

"""

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.d[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if self.d[key][m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1

        if l == 0:
            return ""

        return self.d[key][l - 1][1]
