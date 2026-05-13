class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def bt(n):
            if n == 1 or n == 0:
                return 1
            if n in memo:
                return memo[n]
            memo[n-1]  = bt(n-1)
            memo[n-2] = bt(n-2)
            return memo[n-1] + memo[n-2]
        
        return bt(n)


        # dp = [0 for i in range(n+1)]
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        




# You are given an integer n representing the number of steps to reach the top of a staircase.
# - bounds: [1,n]

# You can climb with either 1 or 2 steps at a time.
# -> my actions: 
#     - step once
#     - step twice
#     base case: if n is 1, then return 1

# Return the number of distinct ways to climb to the top of the staircase.