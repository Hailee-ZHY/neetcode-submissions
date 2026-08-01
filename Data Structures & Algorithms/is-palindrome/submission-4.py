class Solution:
    def isPalindrome(self, s: str) -> bool:
        def _helper(c):
            return ord("a") <= ord(c) <= ord("z") or \
                    ord("0") <= ord(c) <= ord("9")

        s = s.lower()
        l, r = 0, len(s)-1
        while l < r:
            while not _helper(s[l]) and l < r:
                l += 1
            
            while not _helper(s[r]) and r > l:
                r -= 1
            
            if s[l] != s[r]:
                return False
            else:
                l+= 1
                r-=1
        return True
            