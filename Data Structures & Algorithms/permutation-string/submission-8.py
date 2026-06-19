class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        cnt1, cnt2 = [0]*26, [0]*26
        for i in range(n1):
            cnt1[ord(s1[i])-ord("a")] += 1
            cnt2[ord(s2[i])-ord("a")] += 1
        
        if cnt1 == cnt2:
            return True

        for j in range(n1, n2):
            cnt2[ord(s2[j])-ord("a")] += 1
            cnt2[ord(s2[j-n1])-ord("a")] -= 1
            
            if cnt1 == cnt2:
                return True
        return False