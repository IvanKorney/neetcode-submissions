class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        def can_eat(speed):
            hours = sum(math.ceil(pile/speed) for pile in piles)
            return hours <= h
        
        while l <= r:
            mid = (l+r)//2
            if can_eat(mid):
                r = mid-1
            else:
                l = mid+1

        return l