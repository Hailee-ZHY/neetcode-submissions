# calrify questions: If an element appears multiple times, does each occurrence count toward its frequency

# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for i in nums: #O(n)
            cnt[i] = cnt.get(i, 0) + 1
        
        freq = [[] for _ in range(len(nums)+1)]
        for v, c in cnt.items():
            freq[c].append(v)
        
        res = []
        for i in range(len(freq)-1, -1, -1): 
            if len(res) >= k:
                return res
            res.extend(freq[i])
        return res