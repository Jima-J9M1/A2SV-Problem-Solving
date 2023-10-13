class Solution:
    def countOrders(self, n: int) -> int:
        
        def dp(n):
            if n == 1:
                return 1
            
            
            res = n * ((2*n - 1) * dp(n - 1))
            
            return res
        
        ans = dp(n)
        
        return ans % 1_000_000_007
    