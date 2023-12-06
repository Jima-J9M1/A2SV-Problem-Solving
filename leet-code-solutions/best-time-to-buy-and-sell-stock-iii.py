class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        @cache
        def dp(pos, bought, trans):
            if pos >= n or trans == 0:
                return 0
            
            res = dp(pos + 1, bought, trans)
            
            if bought:
                res = max(res, dp(pos + 1, False, trans - 1) + prices[pos])
            else:
                res = max(res, dp(pos + 1, True, trans) - prices[pos])
                
            return res
        
        
        ans = dp(0, False, 2)
        
        return ans