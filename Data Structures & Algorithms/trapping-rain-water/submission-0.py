class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0 for _ in range(len(height))]
        maxLeft[0] = 0

        res = [0 for _ in range(len(height))]

        maxRight = [0 for _ in range(len(height))]
        maxRight[-1] = 0

        for i in range(1, len(height)):
           maxLeft[i] = max(height[:i])
        for j in range(len(height)-2, -1, -1):
           maxRight[j] = max(height[j+1:])

        for i in range(len(height)):
            res[i] = max(min(maxLeft[i], maxRight[i]) - height[i], 0)
        
        return sum(res)