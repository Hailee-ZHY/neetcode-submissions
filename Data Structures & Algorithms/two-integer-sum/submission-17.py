# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counterpart = {} # key: value, value: index
        for i, v in enumerate(nums):
            if target - v in counterpart:
                return [counterpart[target - v], i]
            else:
                counterpart[v] = i
        return False