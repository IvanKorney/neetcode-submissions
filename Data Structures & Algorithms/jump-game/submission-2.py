class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = len(nums)-1
        for i in range(jump,-1,-1):
            if nums[i] + i >= jump:
                jump = i
            

        return jump == 0