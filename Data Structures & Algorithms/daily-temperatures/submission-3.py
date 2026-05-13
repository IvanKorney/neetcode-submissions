class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            count = 0
            for j in range(i,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = count
                    break
                else:
                    count += 1
        return res
