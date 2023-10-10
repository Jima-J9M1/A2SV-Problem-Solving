class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_hash = 0
        subarry_hash = 0
        
        for indx, ch in enumerate(needle):
            ch_num = ord(ch) - ord('a') + 1
            expo = len(needle) - (indx + 1)
            needle_hash += ch_num * 26**(expo)
            
        needle_hash %=  1_000_000_007
        left = 0
        right = len(needle)
        
        while right <= len(haystack):
            indx = left
            subarry_hash = 0
            for i in range(len(needle)):
                ch_num = ord(haystack[indx]) - ord('a') + 1
                expo = len(needle) - (i + 1)
                subarry_hash += ch_num * 26**(expo)
                indx += 1
                
            subarry_hash = subarry_hash % 1_000_000_007
            if subarry_hash == needle_hash:
                return left
                break
                
            left += 1
            right += 1
            
    
        return -1
        