# time complexity: O(nlogn)
# space complexity: O(n)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_revert = [-i for i in stones]
        heapq.heapify(stone_revert)

        while len(stone_revert) >= 2:
            x = heapq.heappop(stone_revert)
            y = heapq.heappop(stone_revert)

            if x != y:
                delta = abs(x-y)
                heapq.heappush(stone_revert, -delta)
        
        if not stone_revert:
            return 0 
        else:
            return -stone_revert[0]
