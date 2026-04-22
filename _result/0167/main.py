"""
167. Two Sum II - Input Array Is Sorted

条件
l + r = target を探す
成立する l, r を返す

注意
必ず成立する組み合わせが存在する

思考
同じ数字の場合はスキップしたい
set使えそう
けど、定数化はメモリ食うし、set(numbers)は長いから好まない
→ 同じ数字来た時に早期リターンする
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target and l < r:
            if l > 0 and numbers[l] == numbers[l - 1]:
                l += 1
                continue
            if r < len(numbers) - 1 and numbers[r] == numbers[r + 1]:
                r -= 1
                continue

            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] > target:
                r -= 1

        return [l + 1, r + 1]