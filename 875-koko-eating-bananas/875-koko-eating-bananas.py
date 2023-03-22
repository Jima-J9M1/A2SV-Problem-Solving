class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        
        #Function that check if koko finished all banana within the given time 
        #if she ate some banana within an hour
        def check(banana):
            hour = 0
            
            for ele in piles:
                hour += (math.ceil(ele / banana))
                
                if hour > h:
                    return False
            return True
        
        left = 1
        right = piles[-1]
        
         
        
        
        while left < right:
            
            mid = left + (right - left) // 2
            
            #check if the mid is valid 
            if check(mid):
                right = mid
                
            else:
                left = mid + 1
                
        return left