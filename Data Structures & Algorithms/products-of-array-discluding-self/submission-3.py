class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [0] * len(nums)
        rightProduct = [0] * len(nums)

        # left
        leftInitial = 1 
        for i in range(len(nums)):
            leftInitial = leftInitial * nums[i]
            leftProduct[i] = leftInitial
        # right
        rightInitial = 1 
        for i in range(len(nums)-1, -1, -1):
            rightInitial = rightInitial * nums[i]
            rightProduct[i] = rightInitial
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = rightProduct[i+1]
            elif i == len(nums)-1:
                res[i] = leftProduct[i-1]
            else:
                 res[i] = leftProduct[i-1] * rightProduct[i+1]

        return res             