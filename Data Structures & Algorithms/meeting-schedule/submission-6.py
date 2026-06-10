"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        holder = []
        heapq.heapify(holder)

        # rerank the list
        for i in intervals:
            heapq.heappush(holder, (i.start, i.end))
        
        prev_start, prev_end = heapq.heappop(holder)

        while holder:
            curr_start, curr_end = heapq.heappop(holder)
            if curr_start < prev_end:
                return False
            prev_start, prev_end = curr_start, curr_end
        return True