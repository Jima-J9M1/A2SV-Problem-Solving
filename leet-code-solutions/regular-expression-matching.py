class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            
            if (i, j) in memo:
                return memo[i, j]
            
            
            check_dot = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            if j  + 1 < len(p) and p[j + 1] == "*":
                ans = dp(i, j + 2) or check_dot and dp(i + 1, j)
            else:
                ans = check_dot and dp(i + 1, j + 1)
                
            memo[i, j] = ans
            
            
            return memo[i, j]
        
        return dp(0, 0)
        
        
        