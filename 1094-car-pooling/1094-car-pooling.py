class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        num_trips = [0] * 1002
        
        for i in range(len(trips)):
            num_pass,l,r = trips[i]
            
            num_trips[l] += num_pass
            num_trips[r] -= num_pass
        
        for i in range(1,len(num_trips)):
            num_trips[i] += num_trips[i - 1]
            
    
        return max(num_trips) <= capacity