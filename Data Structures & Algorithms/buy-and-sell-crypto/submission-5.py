class Solution:
    def maxProfit(self, p: List[int]) -> int:
        res = 0
        l,r = 0,0
        while r < len(p):
            profit = p[r] - p[l]
            if profit > res:
                res = profit
            elif profit < 0:
                l = r
            r += 1
        return res
        