class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        first = [-1] * 26
        last =  [-1] * 26
        
        
        for i in range(len(s)):
            indx = ord(s[i]) - ord('a')
            
            if first[indx] == -1:
                first[indx] = i
                
            last[indx] = i
            
        ans = 0
        
        for i in range(26):
            if first[i] == -1:
                continue
                
            between = set()
            
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])
                
            ans += len(between)
            
            
        return ans
#         letters =set(s)
        
#         ans = 0
        
#         for letter in letters:
#             i, j = s.index(letter), s.rindex(letter)
#             between = set()
            
#             for k in range(i + 1, j):
#                 between.add(s[k])
                
#             ans += len(between)
            
            
#         return ans