class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        text1 = s
        text2 = s[::-1]
        
        def dp(i, j):
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i >= len(text1) or j >= len(text2):
                return 0
            
            
            if text1[i] == text2[j]:
                ans = 1 + dp(i + 1, j + 1)
                memo[(i, j)] = ans
                
            else:
                ans1 = dp(i, j + 1)
                ans2 = dp(i + 1, j)
                memo[(i, j)] = max(ans1, ans2)
            
            
            return memo[(i, j)]
            
        res = dp(0, 0)
        
        return res