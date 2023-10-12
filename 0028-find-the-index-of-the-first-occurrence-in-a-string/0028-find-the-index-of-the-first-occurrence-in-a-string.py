class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        def LPSFunction(st):
            prevLPS = 0
            i = 1
            
            LPS = [0]*len(st)
            
            while i < len(st):
                if st[prevLPS] == st[i]:
                    LPS[i] = prevLPS + 1
                    prevLPS += 1
                    i += 1
                    
                else:
                    if prevLPS == 0:
                        i += 1
                        
                    else:
                        prevLPS = LPS[prevLPS - 1]
                        
                        
            return LPS
        
        
        LPS = LPSFunction(needle)
        
        needle_ptr = 0
        hay_ptr = 0
        
        while hay_ptr < len(haystack) and needle_ptr < len(needle):
            if needle[needle_ptr] == haystack[hay_ptr]:
                needle_ptr += 1
                hay_ptr += 1
                
            else:
                if needle_ptr == 0:
                     hay_ptr += 1
                    
                else:
                    needle_ptr = LPS[needle_ptr - 1]
             
        
        if needle_ptr == len(needle) and hay_ptr >= len(needle):
            return hay_ptr - needle_ptr
        
        return -1
            
            
            
            