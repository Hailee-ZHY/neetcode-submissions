class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumHolder = []

        def dfs(currSum: int, op: list[str], idx: int):
            if idx > (len(nums)-1):
                sumHolder.append(currSum)
                return 

            for i in op:
                if i == "add":
                    currSum += nums[idx]
                else:
                    currSum -= nums[idx]
                
                dfs(currSum, op, idx+1)

                if i == "add":
                    currSum -= nums[idx]
                else:
                    currSum += nums[idx]
        dfs(0, ["add", "sub"], 0)
            
        return sum(1 for i in sumHolder if i == target)