class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        LastIndex = {} # char ->last index
        for i, c in enumerate(s):
            LastIndex[c] = i
        
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, LastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res 