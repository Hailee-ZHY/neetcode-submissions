# 2-DP solution

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        holder = [[0] * len(coins) for _ in range(amount+1)]
        holder[0] = [1] * len(coins)

        for i in range(len(coins)-1, -1, -1):
            for j in range(1, amount+1, 1):
                if coins[i] > j and i == (len(coins)-1):
                    continue 
                
                if i == (len(coins)-1):
                    holder[j][i] = holder[j-coins[i]][i]
                else:
                    holder[j][i] = holder[j-coins[i]][i] + holder[j][i+1]
        return holder[amount][0]