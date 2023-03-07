class Solution:
    def decodeString(self, s: str) -> str:
        
        return self.decode(s)
    
    def decode(self,s):
        ptr = 0
        res = ""
        while ptr < len(s):
            
            if s[ptr].isdigit():
                num = ""
                str_val = ""
                count = 0
                
                while ptr < len(s) and s[ptr] != "[":
                    num += s[ptr]
                    ptr += 1
                    
                #s[ptr] == "[" so increament the ptr by one and add your open brace by one
                ptr += 1
                count  += 1
                
                while ptr < len(s) and count:
                    if s[ptr] == "[":
                        count += 1
                    elif s[ptr] == "]":
                        count -= 1
                    str_val += s[ptr]
                        
                    ptr += 1
                    
                ptr -= 1
                
                res += self.decode(str_val[:-1]) * int(num)
            
            else:
                res += s[ptr]
                
            ptr += 1
        
        return res