class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # the next is lower, next_height * next_index
        # the next is higher, lowest height * next_index, or  area of this one 

        area = 0 # update it
        stack = [] # stor the lowest height: (index, height)

        for i, h in enumerate(heights):
            start = i 
            while stack and h < stack[-1][1]:
                start = stack[-1][0]
                area = max((i-start) * stack[-1][1], area)
                stack.pop()

            stack.append((start, h))
        
        if not stack:
            return area
        
        end = len(heights)
        for rest in stack:
            area = max(area, (end-rest[0])*rest[1])
        return area


