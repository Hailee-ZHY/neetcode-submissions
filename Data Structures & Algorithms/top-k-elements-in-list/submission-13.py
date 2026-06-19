class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use hash map to get the freq
        # for loop, update 
        cnt = defaultdict(int)
        for i in nums:
            cnt[i] += 1 
        
        hold = []
        for value, freq in cnt.items():
            heapq.heappush(hold, (freq, value))
            if len(hold) > k:
                heapq.heappop(hold)
        
        result = [0]*k
        for i in range(k-1,-1,-1):
            result[i] = heapq.heappop(hold)[1]
        return result