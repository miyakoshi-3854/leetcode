class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_lists = set()

        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result_lists.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif nums[i] + nums[l] + nums[r] <= 0:
                    l += 1
                else:
                    r -= 1

        return [list(tup) for tup in result_lists]
