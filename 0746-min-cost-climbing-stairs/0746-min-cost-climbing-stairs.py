class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dp(indx):
            if indx >= len(cost):
                return 0
            
            
            for i in range(indx, len(cost)):
                step1 = dp(indx + 1)
                step2 = dp(indx + 2)
                
                
                
            return min(step1, step2) + cost[indx]
        
        
        step1 = dp(0)
        step2 = dp(1)
        
        return min(step1, step2)