class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holder = {}
        for i in nums:
            if i in holder:
                return True
            else:
                holder[i] = 1
        return False