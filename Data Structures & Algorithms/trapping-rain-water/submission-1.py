class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0,0
        maxLeft = [0]*n
        maxRight = [0]*n
        for i in range(n):
            j = -i-1
            maxLeft[i] = l
            maxRight[j] = r
            r = max(height[j],r)
            l = max(height[i],l)

        
        a = [0]*n
        for i in range(n):
            potential = min(maxLeft[i],maxRight[i])
            actual = max(potential-height[i],0)
            a[i] = actual
        return sum(a)

