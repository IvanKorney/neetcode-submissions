"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def ssort(node):
            return node.start
        intervals.sort(key=ssort)
        pe, ps = -1,-1
        for node in intervals:
            s,e = node.start, node.end
            if s < pe:
                return False
            else:
                ps = s
                pe = e

        return True