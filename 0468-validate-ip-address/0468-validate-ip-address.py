class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if not queryIP:
            return 'Neither'
        
        ans = "Neither"
        
        if queryIP[-1] == '.' or queryIP[-1] == ':' or (queryIP.count(':') != 7 and queryIP.count(':') != 0) or (queryIP.count('.') != 3 and queryIP.count('.') != 0):
            ans = "Neither"
            return ans
            
        
        if "." in queryIP:
            
            IPv4 = queryIP.split('.')
            
            for mask in IPv4:
                if not mask.isdigit() or (len(mask) > 1 and mask[0] == '0'):
                    ans = "Neither"
                    break 
                    
                if len(mask) > 4 or len(mask) == 0:
                    ans = "Neither"
                    break
                    
                if mask.isdigit() and int(mask) < 256:
                    ans = 'IPv4'
                else:
                    ans = 'Neither'
                    break
        else:
            
            IPv6 = queryIP.split(':')
            flag = False
            
            for mask in IPv6:
                if len(mask) > 4 or len(mask) == 0:
                    ans = 'Neither'
                    break
                    
                
                for ch in mask:
                    if ch.isdigit() or ((ch >= 'a' and ch <= 'f') or (ch >= 'A'  and ch <= 'F')):
                        ans = 'IPv6'
                    else:
                        ans = "Neither"
                        flag = True
                        break
                        
                if flag:
                    break
                        
                        
        return ans
                    
                    
                    
                
                    
                    
                
            
            
            
            
            