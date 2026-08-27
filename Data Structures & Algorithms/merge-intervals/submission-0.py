class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key = lambda x : x[0])
        
        # merge intervals
        merged_list = []
        merged_list.append(intervals[0])

        for i in range(1, len(intervals)):
            pre_start, pre_end = merged_list[-1][0], merged_list[-1][1]
            start, end = intervals[i][0], intervals[i][1]

            if start <= pre_end:
                merged_list[-1][1] = max(end, pre_end)

            else:
                merged_list.append(intervals[i])

        return merged_list