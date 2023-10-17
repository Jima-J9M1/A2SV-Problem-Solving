class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
         
        memo = {}
        
        def dp(i):
            if i == len(days):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                
                memo[i] = min(memo[i], c + dp(j))
                
            return memo[i]
                    
        return dp(0)
#         n = days[-1]  # Last day of travel
#         dp = [0] * (n + 1)
#         travel_set = set(days)

#         for i in range(1, n + 1):
#             if i not in travel_set:
#                 dp[i] = dp[i - 1]  # No travel on this day
#             else:
#                 dp[i] = min(
#                     dp[i - 1] + costs[0],                    # 1-day pass
#                     dp[max(0, i - 7)] + costs[1],           # 7-day pass
#                     dp[max(0, i - 30)] + costs[2]           # 30-day pass
#                 )

#         return dp[n]
        