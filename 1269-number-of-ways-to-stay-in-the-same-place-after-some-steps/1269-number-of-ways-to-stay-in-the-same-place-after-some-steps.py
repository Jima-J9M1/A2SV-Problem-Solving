class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def dp(numStep, indxPos):
            if numStep == steps:
                if indxPos == 0:
                    return 1
                else:
                    return 0
                
            if indxPos >= arrLen or indxPos < 0:
                return 0
            
            ans = dp(numStep + 1, indxPos)
            ans += dp(numStep + 1, indxPos - 1)
            ans += dp(numStep + 1, indxPos + 1)
            
            
            return ans
        
        
        result = dp(0,0) % 1_000_000_007
        
        return result
                