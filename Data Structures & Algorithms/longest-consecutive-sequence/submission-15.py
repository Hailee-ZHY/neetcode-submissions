class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxLen = 0 
        
        for i in nums:
            subLen = 1
            if i-1 in setNums:
                continue 
            else:
                while i + subLen in setNums:
                    subLen += 1
                maxLen = max(maxLen, subLen)
        return maxLen 
