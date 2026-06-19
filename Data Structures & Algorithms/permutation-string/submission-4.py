class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        l, r = 0, k-1

        while r < len(s2):
            if self.isPermutation(s1, s2[l:r+1]):
                return True
            else:
                l += 1
                r = l+k-1
        return False

    def isPermutation(self, s1, s2):
        cnt1 = [0]*26
        cnt2 = [0]*26
        for i, j in zip(s1,s2):
           cnt1[ord(i)-ord("a")] += 1
           cnt2[ord(j)-ord("a")] += 1
        return cnt1 == cnt2
