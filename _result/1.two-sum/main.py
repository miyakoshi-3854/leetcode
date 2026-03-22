from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.check(nums, target)
        
    # targetからlist[i]を引いた数が、list[j]に一致するかをみる
    def check(self, nums: list[int], target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()
    result = s.twoSum(nums, target)

    print(result)