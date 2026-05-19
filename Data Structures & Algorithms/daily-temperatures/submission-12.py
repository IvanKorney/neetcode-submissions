class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0]*n
        stack = []

        for i,v in enumerate(temp):
            while stack and stack[-1][1] < v:
                stackI, _ = stack.pop()
                res[stackI] = i - stackI
            
            stack.append((i,v))
        
        return res




