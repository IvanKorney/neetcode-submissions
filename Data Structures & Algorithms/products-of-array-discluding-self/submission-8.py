class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r = 1,1
        n = len(nums)

        res = [1]*n

        for i in range(n):
            res[i] = l
            l *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= r
            r *= nums[i]

        return res