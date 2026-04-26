class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 最初の考え
        # ノードを使って見るindexを変えていく
        # 見たノードを一つ格納する
        # 格納したノードを次のノードと一致するか検証する
        # 検証した数をカウントする
        # カウントした数を大きい場合に書き換える
        # 結果を出力する

        # ソリューションを見た後の考え
        # set変数を用意する
        # result変数を用意する
        # 左、右のポインタを用意する
        # 見る範囲をひとつづつ右へずらしていく
        # set変数が、右のポインタと一致したら、setの重複を消して、左のポインタをtrue分右に動かす
        # これを文字列の最後までやって、result出力

        charSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            result = max(result, right - left + 1)

        return result
