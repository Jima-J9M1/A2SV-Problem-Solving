class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        len_1 = len(str1)
        len_2 = len(str2)
        
        
        val_1 = str1 + str2 
        val_2 = str2 + str1
        
        if val_2 != val_1:
            return ""
        
        idx = math.gcd(len_1, len_2)
        
        return str1[:idx]
        
        