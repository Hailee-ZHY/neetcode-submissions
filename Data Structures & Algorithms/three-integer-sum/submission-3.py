# 如果想用two pointer的话，一定要有序
# .sort()的时间复杂度是O(nlogn)
# 有一个小tricky的点就是排序之后的顺序是有意义的，也就是说如果第一个数是正数的话，后面的数不可能是负数了，那相加也就不可能为0了

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort() # O(nlogn)
        # hold = collections.defaultdict(set) # key: int, value(set(pair))

        for i, v in enumerate(nums):
            if v > 0 or (v == nums[i-1] and i > 0):
                continue 
            else:
                target = 0-v
                l, r = i+1, n-1
                while l < r:
                    if nums[l] + nums[r] == target :
                        res.append([v, nums[l], nums[r]])
                        l += 1 
                        r -= 1 
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1 
        return res

