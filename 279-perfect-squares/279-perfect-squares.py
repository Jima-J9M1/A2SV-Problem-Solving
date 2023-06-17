class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, 101)]
        dp = [float("inf")]*(n + 1)
        dp[0] = 0
        length = len(dp)
        
        for i in range(length):
            for j in range(len(squares)):
                if squares[j] <= i:
                    dp[i] = min(dp[i], 1 + dp[i - squares[j]])
                    
        return dp[n]
#         memo = {}
#         length = len(squares)
        
#         def dp(amount):
#             if amount == 0:
#                 return 0
#             if amount in memo:
#                 return memo[amount]
            
#             if amount < 0:
#                 return float("inf")
            
#             count = float("inf")
#             for i in range(length):
#                 if amount - squares[i] < 0:
#                     break
                    
#                 count = min(count, 1 + dp(amount - squares[i]))
                
#             memo[amount] = count
            
#             return memo[amount]
        
#         dp(n)
        
        
#         return memo[n]
