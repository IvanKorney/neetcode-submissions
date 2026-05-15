class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canEat(speed):
            s = sum(math.ceil(p/speed) for p in piles)
            return s <= h
        
        while l <= r:
            m = (l+r)//2
            if canEat(m):
                r = m - 1
            else:
                l = m + 1

        return l 