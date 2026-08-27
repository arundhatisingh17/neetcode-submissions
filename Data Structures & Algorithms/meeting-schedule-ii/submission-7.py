"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # use the normal approach when they ask you how many meetings to remove or merge
        # use different approach when asked number of meeting rooms

        start = []
        end = []

        num_meeting_rooms = 0
        max_rooms = 0

        if len(intervals) == 0:
            return 0

        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)

        start = sorted(start)
        end = sorted(end)

        s = 0
        e = 0

        while (s < len(start) and s >= 0 and e < len(end)):
            if start[s] >= end[e]:
                num_meeting_rooms -= 1
                e += 1

            else:
                while s < len(start) and s >= 0 and start[s] < end[e]:
                    num_meeting_rooms += 1
                    max_rooms = max(max_rooms, num_meeting_rooms)
                    s += 1

        return max_rooms

