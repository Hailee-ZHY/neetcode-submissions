class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt_hash = {}
        for i in nums:
            if i in cnt_hash:
                cnt_hash[i] += 1 
            else:
                cnt_hash[i] = 1
        
        for values in cnt_hash.values():
            if values > 1:
                return True 
        return False