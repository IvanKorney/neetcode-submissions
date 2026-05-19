class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        memo = {}
        n = len(nums)
        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            skip = dfs(i+1)
            take = dfs(i+2) + nums[i]
            memo[i] = max(skip,take)
            return memo[i]
        return dfs(0)