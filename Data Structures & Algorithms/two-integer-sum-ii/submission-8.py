class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l <= r:
            v = nums[l]+nums[r]
            if v < target:
                l += 1
            elif v > target:
                r -= 1
            else:
                return [l+1,r+1]