# 这一题就是要注意right的起点在哪里
# time complexity: 
# space complexity:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def _helper_cnt(s): #O(n),O(26)
            cache = [0] * 26
            for i in s:
                cache[ord(i) - ord("a")] += 1
            return cache
        
        s1_cnt = _helper_cnt(s1)
        
        left = 0 
        right = left + len(s1)

        while right <= len(s2):
            if _helper_cnt(s2[left:right]) == s1_cnt:
                return True 
            left += 1 
            right = left + len(s1)

        return False
            