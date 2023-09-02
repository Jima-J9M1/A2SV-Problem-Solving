class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #Given: S -> string and dictionary -> list
        # Break S into one or more non-overlapping substring, each substring is present in dictionary.
        # There may be some extra characters in s which are not present in any of the substrings.
        
        #Goal: return the minimum number of extra characters
        #Approach
        memo = {}
        n, dictionary_set = len(s), set(dictionary)
        # @cache
        def dp(start):
            if start == n:
                return 0
            if start in memo:
                return memo[start]
            # To count this character as a left over character 
            # move to index 'start + 1'
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
                    
            memo[start] = ans
            
            return memo[start]
            
        return dp(0)