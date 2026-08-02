# 不用考虑下一个是更长还是更短，对这一题并没有意义

# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV = 0
        l, r = 0, len(heights)-1

        while l < r:
            currV = min(heights[l], heights[r]) * (r-l)
            maxV = max(maxV, currV)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxV