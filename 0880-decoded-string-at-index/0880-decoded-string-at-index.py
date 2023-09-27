class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        indx = 0
        
        
        while length < k:
            if s[indx].isdigit():
                length *= int(s[indx])
            else:
                length += 1
                
            indx += 1
            
        ptr = indx - 1
        
        print(len(s), indx)
        while ptr >= 0:
            if s[ptr].isdigit():
                length //= int(s[ptr])
                k %= length
                
            else:
                if k == 0 or length == k:
                    return s[ptr]
                
                length -= 1
                
            ptr -= 1
                
                
                
                