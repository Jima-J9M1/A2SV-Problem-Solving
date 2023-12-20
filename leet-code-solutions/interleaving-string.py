class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        
        @cache
        def dp(i,j, z):
            if(i >= len(s1) and j >= len(s2)) and z >= len(s3):
                return True
            
            if i >= len(s1) and j >= len(s2):
                return False
            
            if z >= len(s3):
                return False
            
            ans = False
            if (i < len(s1) and s1[i] == s3[z]) and (j < len(s2) and s2[j] == s3[z]):
                ans = ans or (dp(i + 1, j, z + 1) or dp(i, j + 1, z + 1))
                
            elif i < len(s1) and s1[i] == s3[z]:
                ans = ans or dp(i + 1, j, z + 1)
            elif j < len(s2) and s2[j] == s3[z]:
                ans = ans or dp(i, j + 1, z + 1)
            else:
                return False
            
            return ans
        
        res = dp(0, 0, 0)
        
        return res