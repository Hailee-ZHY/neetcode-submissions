class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = {} # {number: index}

        for i in range(len(nums)):
            if target - nums[i] in holder:
                return [holder[target-nums[i]], i]
            else:
                holder[nums[i]] = i 