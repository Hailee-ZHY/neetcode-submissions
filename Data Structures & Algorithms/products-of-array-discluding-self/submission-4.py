# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftTrack = [0]*len(nums)
        rightTrack = [0]*len(nums)

        leftInitial = 1
        for i in range(len(nums)):
            leftInitial = leftInitial * nums[i]
            leftTrack[i] = leftInitial

        rightInitial = 1
        for j in range(len(nums)-1, -1, -1):
            rightInitial = rightInitial * nums[j]
            rightTrack[j] = rightInitial
        
        for k in range(len(nums)):
            if k == 0:
                nums[k] = rightTrack[k+1]
            elif k == len(nums)-1:
                nums[k] = leftTrack[k-1]
            else:
                nums[k] = leftTrack[k-1] * rightTrack[k+1]
        
        return nums