class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        ptr2 = 0
        while ptr < len(s) and ptr2 < len(t):
            if t[ptr2] == s[ptr]:
                ptr += 1
                
            ptr2 += 1 
            
        if ptr >= len(s):
            return True
        
        return False