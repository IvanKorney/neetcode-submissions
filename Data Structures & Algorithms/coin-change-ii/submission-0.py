class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def bt(i,x):
            if (i,x) in memo:
                return memo[(i,x)]
            if i == len(coins) or x > amount:
                return 0
            if x == amount:
                return 1
            take = bt(i,x+coins[i])
            skip = bt(i+1,x)
            memo[(i,x)] = take + skip
            return memo[(i,x)]
        
        return bt(0,0)
       