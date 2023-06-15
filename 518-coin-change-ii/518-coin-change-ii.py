class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count = [0] * (amount + 1)
        res = [float("inf")] * (amount + 1)
        res[0] = 0
        count[0] = 1
        n = len(coins)
        
        for i in range(n):
            for j in range(coins[i], (amount + 1)):
                if res[j - coins[i]] != float("inf"):
                    res[j] = min(res[j], 1 + res[j - coins[i]])
                    count[j] += count[j - coins[i]]
                    
                    
        return count[amount]