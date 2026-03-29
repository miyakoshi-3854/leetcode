class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 単純に配列を結合して真ん中の値を返せばいいのか？
            # 違うみたい
        # とりあえず、nums1, nums2それぞれ半分に分けてみる？
            # 二分探索という方法を使いたいらしい。
            # でもどのように活用したいんだろう？
            # 本当にわからん
        
        sumList = nums1 + nums2
        sumList.sort()

        listLength = len(sumList)
        halfLength = listLength // 2

        if listLength % 2 == 1:
            return sumList[halfLength]
        else:
            return (sumList[halfLength - 1] + sumList[halfLength]) / 2
