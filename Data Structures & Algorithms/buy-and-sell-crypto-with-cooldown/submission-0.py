class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key = (idx, buying), value = max profit

        def dfs(idx: int, buying: bool):
            if idx >= len(prices):
                return 0
            
            if (idx, buying) in dp:
                return dp[(idx, buying)]
            
            if buying:
                buy = dfs(idx+1, not buying) - prices[idx]
                cooldown = dfs(idx+1, buying)
                dp[(idx, buying)] = max(buy, cooldown)
            else:
                sell = dfs(idx+2, not buying) + prices[idx]
                cooldown = dfs(idx+1, buying)
                dp[(idx, buying)] = max(sell, cooldown)
            
            return dfs(idx, buying)
        
        return dfs(0, True)

        