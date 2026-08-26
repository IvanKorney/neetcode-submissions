class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prevS, prevE = float("-inf"), float("-inf")
        res = 0

        for s,e in intervals:
            if s < prevE:
                res += 1
            else:
                prevE = e
                prevS = s


        return res