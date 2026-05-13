class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        for i, v in enumerate(temperatures):
            while stack and stack[-1][1]< v:
                stackI,_ = stack.pop()
                res[stackI] = i-stackI
            stack.append([i,v])
        return res