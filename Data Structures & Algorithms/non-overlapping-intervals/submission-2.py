class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        len_intervals = []

        # sort by start time of the meetings
        intervals = sorted(intervals, key = lambda x : x[0])
        intervals = sorted(intervals, key = lambda x : x[1])

        len_intervals.append(intervals[0])

        for i in range(1, len(intervals)):
            prev_start = len_intervals[-1][0]
            prev_end = len_intervals[-1][1]

            start = intervals[i][0]
            end = intervals[i][1]

            if start < prev_end:
                continue
            else:
                len_intervals.append(intervals[i])


        return len(intervals) - len(len_intervals)