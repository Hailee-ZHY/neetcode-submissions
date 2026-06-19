class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        holder = {} # {cnt: str}
        for i in strs:
            if self.freq(i) in holder:
                holder[self.freq(i)].append(i)
            else:
                holder[self.freq(i)] = [i]
        
        res = []
        for k in holder.values():
            res.append(k)
        return res 

    def freq(self, strs: str) -> list:
        cnt = [0]*26
        for i in strs:
            cnt[ord(i)-ord("a")] += 1 
        return tuple(cnt)