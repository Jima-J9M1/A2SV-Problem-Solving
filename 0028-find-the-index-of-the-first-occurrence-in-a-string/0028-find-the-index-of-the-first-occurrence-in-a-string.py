class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        
        
        needle_hash = 0
        subarry_hash = 0
        length = len(needle)
        left = 0
        right = length - 1
        
        for indx, ch in enumerate(needle):
            ch_num = ord(ch) - ord('a') + 1
            expo = len(needle) - (indx + 1)
            needle_hash += ch_num * 26**(expo)
         
        for indx in range(length):
            ch_num = ord(haystack[indx]) - ord('a') + 1
            expo = len(needle) - (indx + 1)
            subarry_hash += ch_num * 26**(expo)
         
        needle_hash %= 1_000_000_007
        subarry_hash %= 1_000_000_007
        
        if needle_hash == subarry_hash:
            return left
        
        right += 1
        
        while right < len(haystack):
            ch_num = ord(haystack[left]) - ord('a') + 1
            expo = length - 1
            ch_hash_l = ch_num * 26**(expo)
            left += 1
            subarry_hash -= ch_hash_l
            subarry_hash *= 26
            
            ch_num = ord(haystack[right]) - ord('a') + 1
            expo = 0
            ch_hash_r = ch_num * 26**(expo)
            
            subarry_hash += ch_hash_r
            subarry_hash %= 1_000_000_007
            
            if needle_hash == subarry_hash:
                return left
                break
                
            right += 1
            
        return -1