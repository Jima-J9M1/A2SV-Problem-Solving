class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        
        def palindrome(s,count):
            if (len(s) == 0 or len(s) == 1):
                return True
            
            # else:
            #     return False
            
            if (s[0] == s[-1]):
                return palindrome(s[1:-1],count)
            
            elif count < 1:
                val1 = palindrome(s[1:],count + 1) 
                val2 = palindrome(s[:-1],count + 1) 
                
                if val1 or val2:
                    return True
                else:
                    return False
                
            
            return False
                
        count = 0        
        validPalindrome = palindrome(s,count)
        
        return validPalindrome