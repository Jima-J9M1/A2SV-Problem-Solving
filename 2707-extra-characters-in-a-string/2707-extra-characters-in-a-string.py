class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #Given: S -> string and dictionary -> list
        # Break S into one or more non-overlapping substring, each substring is present in dictionary.
        # There may be some extra characters in s which are not present in any of the substrings.
        
        #Goal: return the minimum number of extra characters
        #Approach
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (n + 1)
         
        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                cur = s[start:end + 1]
                if cur in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1])
                
                
        return dp[0]
#         memo = {}
#         n, dictionary_set = len(s), set(dictionary)
#         # @cache
#         def dp(start):
#             if start == n:
#                 return 0
#             if start in memo:
#                 return memo[start]
#             # To count this character as a left over character 
#             # move to index 'start + 1'
#             ans = dp(start + 1) + 1
#             for end in range(start, n):
#                 curr = s[start: end + 1]
#                 if curr in dictionary_set:
#                     ans = min(ans, dp(end + 1))
                    
#             memo[start] = ans
            
#             return memo[start]
            
#         return dp(0)