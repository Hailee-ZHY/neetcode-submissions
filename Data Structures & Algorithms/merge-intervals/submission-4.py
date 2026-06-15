class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        prev_start, prev_end = intervals[0][0], intervals[0][1]
        res = []
        n = len(intervals)

        for k in range(1, n):
            if intervals[k][0] > prev_end:
                res.append([prev_start, prev_end])
                prev_start, prev_end = intervals[k][0], intervals[k][1]
            else:
                prev_start = min(prev_start, intervals[k][0])
                prev_end = max(prev_end, intervals[k][1])
        res.append([prev_start, prev_end])
        return res