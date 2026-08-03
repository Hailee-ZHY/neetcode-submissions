class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        cache = [] # (key: distance, value = point)
        
        for p in points:
            cache.append((p[0]**2+p[1]**2, p))
        
        heapq.heapify(cache)

        res = []
        while k > 0:
            val = heapq.heappop(cache)
            res.append(val[1])
            k -= 1 
        
        return res

        


