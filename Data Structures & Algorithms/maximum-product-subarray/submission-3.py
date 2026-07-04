class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = currMin = gloMax = nums[0]

        for i in range(1, len(nums)):
            tempMax = currMax
            currMax = max(nums[i], nums[i]*currMax, nums[i]*currMin)
            currMin = min(nums[i], nums[i]*tempMax, nums[i]*currMin)
            if currMax > gloMax:
                gloMax = currMax
        return gloMax

        