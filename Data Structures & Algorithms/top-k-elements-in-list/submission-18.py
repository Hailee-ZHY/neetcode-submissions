class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)] 
        count = {} # {num: cnt}
        
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1 

        for n, c in count.items():
            freq[c].append(n)
        

        res = []
        
        for j in range(len(freq)-1, 0, -1):
            for n in freq[j]:
                res.append(n)
                if len(res) == k:
                    return res