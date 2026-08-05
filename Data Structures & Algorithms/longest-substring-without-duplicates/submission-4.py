class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        left = 0 
        cache = set()
        for right in range(len(s)):
            while s[right] in cache:
                cache.remove(s[left])
                left += 1
            cache.add(s[right])
            longest = max(longest, right - left + 1)

        return longest

