class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i, j, = 0, 0 
        sort_num = []
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sort_num.append(nums1[i])
                i += 1
            else:
                sort_num.append(nums2[j])
                j += 1 
        
        if len(sort_num) < (m+n):
            if  j >= n:
                sort_num.extend(nums1[i:])
            else:
                sort_num.extend(nums2[j:])
        
        # odd
        mid = (m+n)//2
        rest = (m+n) % 2
        if rest != 0:
            return sort_num[mid]
        # even
        else:
            return (sort_num[mid] + sort_num[(mid-1)])/2