class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def dp(direction, numStep, indxPos):
            if numStep == steps:
                if indxPos == 0:
                    return 1
                else:
                    return 0
                
            if indxPos >= arrLen or indxPos < 0:
                return 0
            
            stay = dp(0, numStep + 1, indxPos)
            left = dp(1, numStep + 1, indxPos - 1)
            right = dp(2, numStep + 1, indxPos + 1)
            
            
            return stay + left + right
        
        
        stay = dp(0, 1, 0)
        right = dp(2, 1, 1)
        
        
        return (stay % 1_000_000_007 + right % 1_000_000_007) % 1_000_000_007
                