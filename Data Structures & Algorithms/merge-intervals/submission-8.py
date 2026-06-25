class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # step 1. sort
        intervals.sort(key = lambda x: x[0])

        # step 2. 
        res = []

        l, r = intervals[0][0], intervals[0][1] 

        for i in range(1, len(intervals)):
            if intervals[i][0] <= r:
                r = max(r, intervals[i][1])
            else:
                res.append([l,r])
                l = intervals[i][0]
                r = intervals[i][1]
        res.append([l,r])
        return res 

            
            
