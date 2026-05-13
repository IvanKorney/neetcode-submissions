class Solution:
    def dailyTemperatures(self, ts: List[int]) -> List[int]:
        n = len(ts)
        res = [0]*n
        stack = []

        for i,v in enumerate(ts):
            while stack and v > stack[-1][1]:
                (stackI,_) = stack.pop()
                res[stackI]= i-stackI
            stack.append((i,v))


        return res
