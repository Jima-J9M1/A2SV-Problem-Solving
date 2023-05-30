class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        ans = self.dp(amount, coins, memo)
        
        return ans if ans != float("+inf") else -1
    
    
    def dp(self, amount, coins, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return float("+inf")
        
        if amount not in memo:
            res = float("+inf")
            for i in range(len(coins)):
                
                res = min(res,self.dp(amount - coins[i], coins,memo) + 1)
            
            memo[amount] = res
                
            
        return memo[amount]
    
        
        