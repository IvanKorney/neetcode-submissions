class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def myFunc(n):
            return n[1]
        intervals.sort(key=myFunc)
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]
        return res


                