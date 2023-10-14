class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        memo = {}
        def dp(indx, remain):
            if remain <= 0:
                return 0
            
            if indx == len(cost):
                return inf
            
            if (indx, remain) in memo:
                return memo[(indx, remain)]
            
            paint = cost[indx] + dp(indx + 1, remain - (1 + time[indx]))
            no_paint = dp(indx + 1, remain)
            
            memo[(indx, remain)] = min(paint, no_paint)
            
            return memo[(indx, remain)]
        
        wall = len(cost)
        
        return dp(0, wall)