class Solution:
    def integerBreak(self, n: int) -> int:
        
        
        def dp(n, res, freq):
            if n == 0:
                if freq < 2:
                    return 0
                 
            
                return res

            if (n, res, freq) in memo:
                return memo[(n, res, freq)]
            ans = 0
            for i in range(1, n + 1):
                ans = max(ans, dp(n - i, res * i, freq + 1))
                
            memo[(n, res, freq)] = ans
            return ans 
        
        memo = {}
        result = dp(n, 1, 0)
        
        return result
