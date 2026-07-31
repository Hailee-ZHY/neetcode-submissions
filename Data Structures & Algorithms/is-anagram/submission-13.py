# time complexity: O(m+n)
# space cimplexity: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = [0]*26 # O(1)
        t_cnt = [0]*26

        for i in s:
            s_cnt[ord(i)-ord("a")] += 1 
        
        for j in t:
            t_cnt[ord(j)-ord("a")] += 1 
        
        if s_cnt != t_cnt:
            return False 
        
        return True 
