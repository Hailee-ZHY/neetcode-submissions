class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # edge case1: new interval is bigger than the last one 
        # edge case2: intervals is empty

        if not intervals:
            return [newInterval]

        heapq.heapify(intervals)
        heapq.heappush(intervals, newInterval)
        res = [heapq.heappop(intervals)] # get the first one

        while intervals:
            curr = heapq.heappop(intervals)
            if curr[0] > res[-1][1]:
                res.append(curr)
            else:
                start = min(res[-1][0], curr[0])
                end = max(res[-1][1], curr[1])
                rep = [start, end]
                res[-1] = rep
        return res

