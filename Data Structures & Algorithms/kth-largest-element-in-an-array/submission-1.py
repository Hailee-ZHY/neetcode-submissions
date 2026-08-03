# time complexity: O(NlogK)
# space complexity: O(N)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num_k = nums[:k]
        heapq.heapify(num_k)
        
        for i in nums[k:]:
            if i > num_k[0]:
                heapq.heappop(num_k)
                heapq.heappush(num_k, i)
        return num_k[0]