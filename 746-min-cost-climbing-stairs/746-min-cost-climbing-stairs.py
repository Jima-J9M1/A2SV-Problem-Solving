class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)
        dp[-3] = cost[-1]
        for i in range(len(cost) - 1, -1 , -1):            
            dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]
        return min(dp[0], dp[1])
        
#         memo = {}
#         ans = self.dp(-1, cost, memo)
        
#         return ans
        
#     def dp(self, indx, cost, memo):
#         if indx not in memo:
            
#             if len(cost) <= indx:
#                 return 0


#             first = 0
#             second = 0

#             if (indx + 2) < len(cost):
#                 first = cost[indx + 2] + self.dp(indx + 2, cost, memo)
                


#             if (indx + 1) < len(cost):
#                 second = cost[indx + 1] + self.dp(indx + 1, cost, memo)




#             memo[indx] =  min(first, second)
        
#         return memo[indx]

        