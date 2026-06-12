class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        prev_end = intervals[0][1]
        n = len(intervals)
        res = 0
        
        for k in range(1, n):
            if intervals[k][0] < prev_end:
                res += 1 
                prev_end = min(prev_end, intervals[k][1])
            else:
                prev_end = intervals[k][1]
        return res