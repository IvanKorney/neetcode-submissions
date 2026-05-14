class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def sub(i,s):
            if sum(s) == target:
                res.append(s[:])
                return
            if i == n or sum(s) > target:
                return 
            
            s.append(nums[i])
            sub(i,s)
            s.pop()
            sub(i+1,s)
            


        sub(0,[])
        
        
        return res