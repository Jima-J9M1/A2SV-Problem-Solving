class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        @cache
        def dp(inital, final, length):
            if final > n:
                return float("inf")
            
            if final == n:
                return length
            
            paste = dp(inital, final + inital, length + 1)
            copy_paste = dp(final, 2 * final, length + 2)
            
            return min(copy_paste, paste)
        
        
        ans = dp(1, 2, 2)
        
        return ans