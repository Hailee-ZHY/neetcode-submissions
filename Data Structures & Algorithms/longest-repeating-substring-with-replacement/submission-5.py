class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cache = {} # key: number, value: cnt
        left = 0 
        longest = 0
        for right in range(len(s)):
            cache[s[right]] = cache.get(s[right], 0) + 1
            while (right-left + 1) - max(cache.values()) > k :
                cache[s[left]] -= 1
                left += 1
            longest = max(longest, right-left + 1)
            
        return longest