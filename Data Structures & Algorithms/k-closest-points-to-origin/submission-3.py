class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [i**2+j**2 for i, j in points]
        holder = []
        heapq.heapify(holder)

        for j in zip(distance, points):
            heapq.heappush(holder, j)

        res = []
        while k > 0:
            res.append(heapq.heappop(holder)[1])
            k -= 1
        return res