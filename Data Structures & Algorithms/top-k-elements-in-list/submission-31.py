class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntHash = {}
        for i in nums:
            cntHash[i] = cntHash.get(i, 0) + 1
        
        freq = [[] for i in range(len(nums)+1)]
        
        for n, c in cntHash.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            if freq[i] != 0:
                for j in freq[i]:
                    res.append(j)
                    if len(res) == k:
                        return res