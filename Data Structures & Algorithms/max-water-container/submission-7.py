class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxArea = 0
        l,r = 0, len(h)-1 
        while l < r:
            area = min(h[l],h[r])*(r-l)
            maxArea = max(area,maxArea)
            if h[r] > h[l]:
                l += 1
            else:
                r -= 1
        return maxArea