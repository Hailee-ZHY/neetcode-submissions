class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        lenMax = 0
        for i in nums:
            if i-1 not in nums:
                k = 0
                while i+k in nums:
                    k += 1
                lenMax = max(lenMax, k)
        return lenMax
