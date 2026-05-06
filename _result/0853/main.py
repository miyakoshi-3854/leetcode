"""
853. Car Fleet

条件
ゴール地点に到達する車達のグループがいくつあるか

注意
一直線だから追い越し無し
追いついたら直前のやつと合わせる

思考
stack使う

ゴール時間の計算の仕方
(target - position) / speed

stackに入れるのは、ゴール時間

stackのtopのゴール時間よりも今見ているゴール時間が小さくなった時点で
topのゴール時間として考えていい、何なら置き換えるのがいいか

どうやってグループ分けするのか
置き換えて、同じ数字だったらグループとして換算でいけそう？

ゴールに近いものから処理しないといけない
zip(position, speed)でソートする
o(10 ^ 5)だから間に合う

"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        cars = sorted(zip(position, speed), reverse=True)
        for i in range(len(cars)):
            if fleet and fleet[-1] >= (target - cars[i][0]) / cars[i][1]:
                continue
            fleet.append((target - cars[i][0]) / cars[i][1])

        return len(fleet)
