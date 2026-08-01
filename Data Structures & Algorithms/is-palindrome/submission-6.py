# 在内部的while的时候也要记得判断l和r之间的边界条件，不然容易out of index的问题
# time complexity: 
### 需要注意的一点是，这里的two point, 所以时间复杂度是O(n), Binary Search的时间复杂度才是O(nlogn). Two point的是指针一点点靠近，Binary Search是直接砍掉一半, e.g. mid = (l+r)//2
# space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def _helper(c):
            return ord("a") <= ord(c) <= ord("z") or \
                    ord("A") <= ord(c) <= ord("Z") or \
                    ord("0") <= ord(c) <= ord("9")

        l, r = 0, len(s)-1
        while l < r:
            while not _helper(s[l]) and l < r:
                l += 1
            
            while not _helper(s[r]) and r > l:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                l+= 1
                r-=1
        return True
            