class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_head = self._helper(nums[0:-1])
        max_tail = self._helper(nums[1:])

        return max(max_head, max_tail)

        
    def _helper(self, nums:List[int]) -> int:
        rob1, rob2 = 0 , 0 
        for n in nums:
            temp = max(rob2, rob1+n)
            rob1 = rob2
            rob2 = temp 
        return rob2