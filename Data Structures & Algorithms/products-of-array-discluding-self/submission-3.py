class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        up,down = 1,1

        for i in range(n):
            res[i] = up
            up *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= down
            down *= nums[i]
        return res
