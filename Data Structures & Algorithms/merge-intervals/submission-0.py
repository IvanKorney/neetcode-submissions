class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev_s, prev_e = -1,-1
        res = []
        for s, e in intervals:
            if prev_e == -1:
                prev_s = s
                prev_e = e
            else:
                if s > prev_e:
                    res.append([prev_s,prev_e])
                    prev_s = s
                    prev_e = e
                else:
                    prev_e = max(e,prev_e)
        if prev_e != -1:
            res.append([prev_s,prev_e])
        return res
                