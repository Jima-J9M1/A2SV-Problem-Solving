class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        
        def dp(indx, sum_):
            if indx == len(stones):
                return sum_
            
            if (indx, sum_) in memo:
                return memo[(indx, sum_)]
            
            decrease = dp(indx + 1, abs(sum_ - stones[indx]))
            increase = dp(indx + 1, abs(sum_ + stones[indx]))
            
            memo[(indx, sum_)] = min(decrease, increase)
            
            return memo[(indx, sum_)]
        
        ans = dp(0, 0)
        
        return ans