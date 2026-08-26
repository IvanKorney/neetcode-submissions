class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dfs(i,x):
            if i == n:
                if x == target:
                    return 1
                return 0
            if (i,x) in memo:
                return memo[(i,x)]

            
            add = dfs(i+1,x+nums[i])
            sub = dfs(i+1,x-nums[i])
            memo[(i,x)] = add + sub
            return add + sub
        
        return dfs(0,0)
