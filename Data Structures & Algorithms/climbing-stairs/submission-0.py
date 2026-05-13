class Solution:
    def climbStairs(self, n: int) -> int:
        def ways_toStep(n):
            if n == 1 or n ==0:
                return 1
            stepOnce = 0
            stepTwice = 0
            if n - 1 >= 0:
                stepOnce = ways_toStep(n-1)
            if n-2 >= 0:
                stepTwice = ways_toStep(n-2)
            return stepOnce+stepTwice
        return ways_toStep(n)
        




# You are given an integer n representing the number of steps to reach the top of a staircase.
# - bounds: [1,n]

# You can climb with either 1 or 2 steps at a time.
# -> my actions: 
#     - step once
#     - step twice
#     base case: if n is 1, then return 1

# Return the number of distinct ways to climb to the top of the staircase.