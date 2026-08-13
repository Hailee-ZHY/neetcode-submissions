class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the biggest k will be the length of piles 

        n = len(piles)
        
        """
        1,4,3,2 => 4, 4 < 9 => max
        1,4,3,2 => 3, 5 < 9 
        1,4,3,2 => 2, 6 < 9 
        1,4,3,2 => 1, 10 > 9 => min
        """

        k_min = 1
        k_max = max(piles) # O(n)

        k = k_max
        while k_min <= k_max:
            k_mid = (k_min + k_max) // 2
            h_est = sum([math.ceil(i/k_mid) for i in piles])
            if h_est <= h:
                k = min(k, k_mid)
                k_max = k_mid - 1
            elif h_est > h:
                k_min = k_mid + 1
        return k


