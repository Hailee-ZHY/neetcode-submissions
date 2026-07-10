class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnt = {} # {value: freq}

        for i in nums:
            cnt[i] = cnt.get(i, 0) + 1

        freq = [[] for i in range(len(nums)+1)]

        for v, c in cnt.items():
            freq[c].append(v)

        res = []
        for i in range(len(freq)-1, 0, -1):
            if freq[i] != 0:
                for j in freq[i]:
                    res.append(j)
                    if len(res) == k:
                        return res
                
