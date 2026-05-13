class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def cantJump(i):
            if i >= len(nums)-1:
                return True
            for j in range(1,nums[i]+1):
                if cantJump(i+j):
                    return True
            
        return True if cantJump(0) else False

