class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        #find the minium length of the string
        min_val = min(len(word1), len(word2))
        left = 0
        ans = ""
        
        while left < min_val:
            val = word1[left] + word2[left]
            ans += val
            left += 1
            
            
        if len(word1) > len(word2):
            ans += word1[left :]
        elif len(word2) > len(word1):
            ans += word2[left :]
            
        return ans
        
            
        