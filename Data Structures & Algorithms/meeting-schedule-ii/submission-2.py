"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # minimum number  = how to find the minimum number
        # example: [0,40], [8,50], [45, 50], [50,60]
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        s, e = 0, 0 
        res, count = 0, 0 # res: result, count: the number of room reuiqred now

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1 
                count += 1 
            else:
                e += 1 
                count -= 1
            res = max(res, count)
        return res
        
        