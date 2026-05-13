class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0]*len(t)
        stack = []

        for i, v in enumerate(t):
            while stack and stack[-1][1] < v:
                (stackI,stackV) = stack.pop()
                res[stackI] = i-stackI
            stack.append((i,v))
        return res
