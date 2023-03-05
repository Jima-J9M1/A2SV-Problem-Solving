# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # arr = [x + 1 for x in range(n)] #n == 5 [1,2,3,4,5]
    
        left = 1
        right = n 
        
        #start your left from 1 because the bad start from one and find which side the bad will occur 
        #bellow the half and above the half
        while left < right:
            mid = left + (right - left) // 2
            boolVal = isBadVersion(mid)
            
            #check if the middle val is bad if bad put your right pointer to the middle 
            #if not put your left pointer to the middle plus one
            if boolVal:
                right = mid
            else:
                left = mid + 1
        
        
        return right
                
                
        
            