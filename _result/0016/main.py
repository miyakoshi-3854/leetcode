class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]

                if temp == target:
                    return temp

                if temp < target:
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                elif temp > target:
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1

                if abs(temp - target) < abs(result - target):
                    result = temp

        return result
