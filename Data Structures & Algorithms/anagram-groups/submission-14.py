# time complexity: O(N*m), N is the length of strs and m is the length of s in strs
# space complexity: O(N*L), N is the strings we have in strs and L is the avarage length of strins

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def _helper(s): #O(m)
            cnt = [0]*26
            for i in s:
                cnt[ord(i) - ord("a")] += 1
            return tuple(cnt) 

        substring = {} # key: cnt, value: list(words)
        for i in strs: # O(N)
            if _helper(i) in substring:
                substring[_helper(i)].append(i)
            else:
                substring[_helper(i)] = [i]

        res = []
        for subs in substring.values():
            res.append(subs)
        return res