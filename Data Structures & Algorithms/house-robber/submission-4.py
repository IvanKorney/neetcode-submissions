class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        for i in range(len(nums)-1,-1,-1):
            if i + 2 < len(dp):
                take = nums[i] + dp[i+2]
            else:
                take = nums[i]
            skip = dp[i+1]
            dp[i] = max(take,skip)
        return dp[0]

        
        # memo = {}
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     take = nums[i] + dfs(i+2)
        #     skip = dfs(i+1)
        #     memo[i] = max(take,skip)
        #     return memo[i]
        # return dfs(0)