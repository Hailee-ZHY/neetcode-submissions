class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.count(s) == self.count(t)
    
    def count(self, s: str) -> list[int]:
        cnt = [0]*26
        for i in s:
            cnt[ord(i)-ord("a")] += 1
        return cnt