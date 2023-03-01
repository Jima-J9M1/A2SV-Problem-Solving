class Solution:
    def reverseString(self, s: List[str]) -> None:
        #BASE CASE
        
        
        
        
        def recurssion(s,left,right):
            
            if left >= right:
                return 
            
            s[left],s[right] = s[right],s[left]
            
            recurssion(s,left + 1, right - 1)
        
        
        recurssion(s,0,len(s) - 1)
        
        
        
   

        
