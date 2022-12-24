class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        #compare both string by thier index and find the their difference, return the difference 
        #val in t string
        s = sorted(s)
        t = sorted(t)
        right = 0
        
        while right < len(s):
            if s[right] == t[right]:
                pass
            else:
                return t[right]
            right += 1
            
        return t[right]
        
        