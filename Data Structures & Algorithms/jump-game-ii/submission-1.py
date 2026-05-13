class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        jump = 0
        while(r < len(nums)-1):
            longest = 0
            for i in range(l,r+1):
                longest = max(longest,i+nums[i])
            l = r
            r = longest
            jump += 1
        
        return jump