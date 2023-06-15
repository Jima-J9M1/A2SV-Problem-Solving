class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        res = [float("inf")] * (amount + 1)
        res[0] = 0
        n = len(coins)
        
        for i in range(n):
            for  j in range(coins[i],(amount + 1)):
                if res[j - coins[i]] != float("inf"):
                    res[j] = min(res[j], 1 + res[j - coins[i]])
                    
                    
        return res[amount] if res[amount] != float("inf") else -1
    
            