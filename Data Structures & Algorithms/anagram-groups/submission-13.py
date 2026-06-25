class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        
        holder = {} #{freq: [str1, str2...]}
        for i in strs:
            freq = self.freq(i)
            if freq in holder:
                holder[freq].append(i)
            else:
                holder[freq] = [i]
        
        for i, v in holder.items():
            res.append(v)
        
        return res
                

        
    
    def freq(self, strs:str) -> bool:
        c = [0]*26
        for i in strs:
            c[ord(i)-ord("a")] += 1 
        return tuple(c) 