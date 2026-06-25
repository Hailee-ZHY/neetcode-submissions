class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        holder = {} # {value: index}

        for i, v in enumerate(nums):
            if target - v in holder:
                return [holder[target - v], i]
            else:
                holder[v]= i
