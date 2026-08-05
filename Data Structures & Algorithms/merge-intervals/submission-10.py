class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0]) # time: O(NlogN), space: O(N)

        res = []
        for i in intervals:
            if not res: 
                res.append(i)
            
            if i[0] <= res[-1][1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)
        return res