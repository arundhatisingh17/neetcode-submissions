"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals = sorted(intervals, key = lambda x : x.start)

        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end

            prev_start = intervals[i-1].start
            prev_end = intervals[i-1].end

            if start < prev_end:
                return False

        return True
        