class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums)//2
        ## 这里有一个很关键的点，无论是set还是list, 在作为被遍历对象的时候，内容都是不可以被改变的
        for i in nums:
            dpNext = set()
            for j in dp:
                dpNext.add(i+j)
            dp.update(dpNext) # 合并集合用update
                
        return True if target in dp else False