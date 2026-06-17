class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy algorithm 的解法一般都是把大问题拆分为小问题，在局部的情况的找当前小问题的最优解

        res = 0 
        l = r = 0

        while r < len(nums)-1:
            res += 1
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
            
            l = r + 1 
            r = farthest
        return res
