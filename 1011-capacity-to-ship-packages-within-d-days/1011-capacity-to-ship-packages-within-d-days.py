class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        #check if the capacity of the boats can carry the weights within the given time
        def check(capacity):
            day = 1
            total_sum = 0
            
            for ele in weights:
                total_sum += ele
                
                if total_sum > capacity:
                    total_sum = ele
                    day += 1
                    
                    if day > days:
                        return False
                    
            return True
        
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            
            mid = left + (right - left) // 2
            
            #check if the capacity is valid 
            if check(mid):
                right = mid
                
            else:
                left = mid + 1
        
        return left 