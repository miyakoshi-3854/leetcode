class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]

                if current_sum == target:
                    return current_sum

                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1

        return closest
