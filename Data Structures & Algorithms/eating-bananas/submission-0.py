class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(speed):
            hours = sum(math.ceil(pile/speed) for pile in piles)
            return h >= hours
        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r)//2
            if canEat(mid):
                r = mid -1
            else:
                l = mid +1
        return l