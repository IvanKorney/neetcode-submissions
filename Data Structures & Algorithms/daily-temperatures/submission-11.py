class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0]*n
        stack = []

        for i in range(n):
            while stack and stack[-1][1] < temp[i]:
                (index,_) = stack.pop()
                res[index] = i - index
            stack.append((i,temp[i]))



        return res