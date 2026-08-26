class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            s,e = intervals[i]
            if e < newInterval[0]:
                res.append([s,e])
            elif s > newInterval[1]:
                res.append(newInterval)
                res += (intervals[i:])
                return res
            else:
                newInterval[0] = min(newInterval[0],s)
                newInterval[1] = max(newInterval[1],e)
        res.append(newInterval)        
        return res
